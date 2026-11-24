import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def execute(command, output_dir, label):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        errors="replace",
    )

    (output_dir / f"{label}.stdout.log").write_text(result.stdout)
    (output_dir / f"{label}.stderr.log").write_text(result.stderr)

    return {
        "command": command,
        "exit_code": result.returncode,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--venv", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    venv = Path(args.venv).resolve()
    out = Path(args.out).resolve()

    python = venv / (
        "Scripts/python.exe" if sys.platform == "win32" else "bin/python"
    )

    if not python.is_file():
        parser.error(f"Target interpreter not found: {python}")

    if out == venv or venv in out.parents:
        parser.error("Output directory must be outside the target environment.")

    if out.exists() and any(out.iterdir()):
        parser.error("Use a new or empty output directory.")

    tools = {}
    for name in ("syft", "trivy", "cyclonedx-py"):
        executable = shutil.which(name)
        if not executable:
            parser.error(f"Required command not found: {name}")
        tools[name] = executable

    out.mkdir(parents=True, exist_ok=True)

    report = {
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "target_environment": str(venv),
        "target_python": str(python),
        "input_mode": "installed-environment",
        "versions": {},
        "runs": {},
    }

    version_commands = {
        "python": [str(python), "--version"],
        "syft": [tools["syft"], "version"],
        "trivy": [tools["trivy"], "--version"],
        "cyclonedx-py": [tools["cyclonedx-py"], "--version"],
    }

    for name, command in version_commands.items():
        report["versions"][name] = execute(
            command, out, f"version-{name}"
        )

    inventory_code = """
import importlib.metadata as metadata
import json

items = [
    {"name": d.metadata["Name"], "version": d.version}
    for d in metadata.distributions()
]
print(json.dumps(sorted(items, key=lambda x: x["name"].lower()), indent=2))
"""

    inventory = execute(
        [str(python), "-c", inventory_code],
        out,
        "installed-inventory",
    )
    report["runs"]["installed-inventory"] = inventory

    if inventory["exit_code"] == 0:
        shutil.copyfile(
            out / "installed-inventory.stdout.log",
            out / "installed.json",
        )

    commands = {
        "syft": [
            tools["syft"],
            "scan",
            f"dir:{venv}",
            "-o",
            f"cyclonedx-json={out / 'syft.cdx.json'}",
        ],
        "trivy": [
            tools["trivy"],
            "rootfs",
            "--pkg-types", "library",
            "--format", "cyclonedx",
            "--output", str(out / "trivy.cdx.json"),
            str(venv),
        ],
        "cyclonedx-py": [
            tools["cyclonedx-py"],
            "environment",
            str(python),
            "--output-format", "JSON",
            "--output-file", str(out / "cyclonedx-py.cdx.json"),
        ],
    }

    failed = inventory["exit_code"] != 0

    for name, command in commands.items():
        run = execute(command, out, name)
        sbom = out / f"{name}.cdx.json"

        try:
            data = json.loads(sbom.read_text())
            run["valid_cyclonedx_json"] = (
                data.get("bomFormat") == "CycloneDX"
            )
            run["component_count"] = len(data.get("components", []))
        except (OSError, ValueError, AttributeError):
            run["valid_cyclonedx_json"] = False

        success = (
            run["exit_code"] == 0
            and run["valid_cyclonedx_json"]
        )
        failed |= not success
        report["runs"][name] = run

        print(f"{name}: {'OK' if success else 'FAILED - check logs'}")

    (out / "run.json").write_text(json.dumps(report, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

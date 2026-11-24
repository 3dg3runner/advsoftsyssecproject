# SBOM generator runner

Runs Syft, Trivy, and CycloneDX-Py against a prepared Python virtual
environment and records SBOMs, tool versions, installed inventory, and logs.

**Status:** installed-environment mode only. Manifest mode (RQ4) is not yet implemented.
This script generates inventories only. It does not execute workloads.

## Pinned versions
- Syft 1.57.2
- Trivy 0.76.2
- cyclonedx-bom 9.0.0
- Base image: python:3.12-slim@sha256:191083cdf6c7bda8c76158983163ead5d5cf7b77cf3033e805bb0f5296f51b4b

## Usage
    docker build -t sbom-lab .
    docker run --rm -it -v "$PWD":/work:Z sbom-lab bash

Inside the container (the target venv must be created inside the container):

    python -m venv /tmp/venv-case
    /tmp/venv-case/bin/pip install <packages>
    python run_sboms.py --venv /tmp/venv-case --out artifacts/<run-name>

The output directory must be new or empty. On Fedora with SELinux, keep the `:Z`
on the mount.

## Known note
On a pilot venv (requests + flask), all three tools reported 13 PyPI
packages. Syft also reported 43 non-PyPI components. Filter to `pkg:pypi/`
purls before computing metrics.

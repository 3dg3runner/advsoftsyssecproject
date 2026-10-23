# Program Name: prog_13_plugin_directory_scanner.py
# Description: Plugin Directory Scanner - Scans directory and loads python files dynamically.

import os
import importlib.util

# Ensure a local 'plugins' directory exists with a dummy file for testing
os.makedirs("plugins", exist_ok=True)
with open("plugins/sample_plugin.py", "w") as f:
    f.write("PLUGIN_VERSION = '1.0.0'\n")

for fname in os.listdir("plugins"):
    if fname.endswith(".py"):
        fpath = os.path.join("plugins", fname)
        spec = importlib.util.spec_from_file_location("sample_plugin", fpath)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print(mod.PLUGIN_VERSION)
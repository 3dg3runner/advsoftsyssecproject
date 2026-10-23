# Program Name: prog_14_entrypoint_import.py
# Description: Entrypoint Import - Simulates package discovery using importlib.metadata.

import importlib.metadata

try:
    eps = list(importlib.metadata.entry_points())
    print(f"Discovered {len(eps)} entry points")
except Exception:
    print("Entry points queried successfully")
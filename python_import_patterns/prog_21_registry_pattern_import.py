# Program Name: prog_21_registry_pattern_import.py
# Description: Registry Pattern Import - Central registry mapping identifiers to imports.

import importlib

registry = {}
def register_tool(name, mod_name):
    registry[name] = mod_name

register_tool("calc", "math")
tool_mod = importlib.import_module(registry["calc"])
print(tool_mod.sqrt(25))
# Program Name: prog_10_string_reflection_globals.py
# Description: String Reflection Globals - Binds imported module via globals mapping.

import importlib

globals()["stats"] = importlib.import_module("statistics")
print(globals()["stats"].mean([1, 2, 3]))
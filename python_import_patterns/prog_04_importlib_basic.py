# Program Name: prog_04_importlib_basic.py
# Description: Basic Dynamic Import - Tests runtime dynamic loading using importlib.

import importlib

mod = importlib.import_module("json")
print(mod.dumps({"test": 1}))
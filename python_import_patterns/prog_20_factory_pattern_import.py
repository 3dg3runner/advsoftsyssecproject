# Program Name: prog_20_factory_pattern_import.py
# Description: Factory Pattern Import - Factory function returning dynamically loaded module.

import importlib

def get_adapter(name):
    return importlib.import_module(name)

m = get_adapter("math")
print(m.pi)
# Program Name: prog_15_config_driven_import.py
# Description: Config-Driven Import - Loads modules specified in a config dictionary.

import importlib

config = {"tools": ["math", "random"]}
for tool in config["tools"]:
    mod = importlib.import_module(tool)
    print(tool, type(mod))
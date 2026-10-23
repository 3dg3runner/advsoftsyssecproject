# Program Name: prog_16_cli_arg_import.py
# Description: CLI Arg-Driven Import - Imports module specified via command-line arguments.

import sys
import importlib

if len(sys.argv) > 1:
    mod = importlib.import_module(sys.argv[1])
    print(mod.__name__)
else:
    # Default fallback demo for direct VS Code execution
    mod = importlib.import_module("math")
    print(mod.sqrt(16))
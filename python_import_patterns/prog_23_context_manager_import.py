# Program Name: prog_23_context_manager_import.py
# Description: Context Manager-Triggered Import - Triggers import upon entering context.

import importlib

class ToolContext:
    def __enter__(self):
        self.mod = importlib.import_module("math")
        return self.mod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

with ToolContext() as ctx:
    print(ctx.sqrt(36))
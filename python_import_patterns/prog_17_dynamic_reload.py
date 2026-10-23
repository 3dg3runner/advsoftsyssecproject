# Program Name: prog_17_dynamic_reload.py
# Description: Dynamic Module Reloading - Reloads an imported module via importlib.reload.

import importlib
import math

print(math.sqrt(4))
math = importlib.reload(math)
print(math.sqrt(9))
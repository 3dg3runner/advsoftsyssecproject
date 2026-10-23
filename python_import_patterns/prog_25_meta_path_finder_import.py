# Program Name: prog_25_meta_path_finder_import.py
# Description: Custom Finder/Loader Hook Simulation - Implements custom finder hook.

import sys

class DummyFinder:
    def find_spec(self, fullname, path, target=None):
        return None

sys.meta_path.insert(0, DummyFinder())
import math
print(math.sqrt(64))
sys.meta_path.pop(0)
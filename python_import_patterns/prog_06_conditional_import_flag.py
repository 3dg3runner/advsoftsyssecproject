# Program Name: prog_06_conditional_import_flag.py
# Description: Conditional Import - Imports random conditionally based on a runtime flag.

load_extra = True
if load_extra:
    import random
    print(random.randint(1, 10))
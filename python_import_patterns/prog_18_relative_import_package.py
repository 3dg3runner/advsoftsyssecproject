# Program Name: prog_18_relative_import_package.py
# Description: Relative Import Package - Tests relative import syntax in a subpackage structure.

# To test in VS Code, structure as a package folder with __init__.py and sub.py:
# from .sub import VAL
# print(VAL)

VAL = 100
print(f"Package loaded with value: {VAL}")
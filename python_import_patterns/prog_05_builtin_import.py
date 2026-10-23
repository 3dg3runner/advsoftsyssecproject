# Program Name: prog_05_builtin_import.py
# Description: Built-in __import__() Function - Tests dynamic import via __import__().

mod_name = "math"
m = __import__(mod_name)
print(m.factorial(5))
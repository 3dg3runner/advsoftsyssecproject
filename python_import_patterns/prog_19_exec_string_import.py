# Program Name: prog_19_exec_string_import.py
# Description: Exec String Import - Executes raw string blocks containing import statements.

code_block = "import math\nres = math.ceil(4.2)"
exec(code_block)
print(res) # type: ignore
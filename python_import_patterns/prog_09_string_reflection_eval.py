# Program Name: prog_09_string_reflection_eval.py
# Description: String Reflection eval() - Constructs and executes import via eval().

mod_name = eval('"co" + "lle" + "ctions"')
c = __import__(mod_name).Counter([1, 2, 2])
print(c)
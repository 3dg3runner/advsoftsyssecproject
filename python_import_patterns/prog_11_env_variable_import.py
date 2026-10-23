# Program Name: prog_11_env_variable_import.py
# Description: Environment Variable Import - Conditional import based on os.environ.

import os

os.environ["USE_JSON"] = "true"
if os.environ.get("USE_JSON", "false") == "true":
    import json
    print(json.loads('{"active": true}'))
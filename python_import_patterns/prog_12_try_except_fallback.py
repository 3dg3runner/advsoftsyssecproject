# Program Name: prog_12_try_except_fallback.py
# Description: Try-Except Fallback - Optional dependency with try-except fallback.

try:
    import ujson as serializer # use 'pip install ujson' if a 'Import ujson could not be resolved' warning appears
except ImportError:
    import json as serializer

print(serializer.dumps({"status": "ok"}))
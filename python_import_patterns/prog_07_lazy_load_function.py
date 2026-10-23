# Program Name: prog_07_lazy_load_function.py
# Description: Lazy Load Function - Defers import inside a function body.

def compute_hash(data):
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()

print(compute_hash("hello"))
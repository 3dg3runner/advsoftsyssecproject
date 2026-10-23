# Program Name: prog_08_lazy_load_property.py
# Description: Lazy Load Property - Defers package loading inside a class property.

class IDGenerator:
    @property
    def token(self):
        import uuid
        return str(uuid.uuid4())

print(IDGenerator().token)
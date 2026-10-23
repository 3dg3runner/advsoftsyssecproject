# Program Name: prog_22_submodule_attribute_access.py
# Description: Submodule Attribute Access - Dynamically traverses submodules via getattr.

import xml.etree

et = getattr(getattr(xml, 'etree'), 'ElementTree')
print(et)
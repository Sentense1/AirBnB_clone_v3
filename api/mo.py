#!/usr/bin/python3
"""Testing documentation of a module
"""
import sys
sys.path.append('.')
from importlib import import_module

print(sys.argv)
if len(sys.argv) < 2:
    print("Usage: {} <module_name>".format(sys.argv[0]))
    sys.exit(1)

m_imported = import_module(sys.argv[1])

if m_imported.__doc__ is None:
    print("No module documentation")
else:
    print("OK")

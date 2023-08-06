#!/usr/bin/python3
"""Testing documentation of a module
"""
import sys
import os

# Add the project's root directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, '..'))

from importlib import import_module

if len(sys.argv) != 2:
    print("Usage: {} module_name".format(sys.argv[0]))
    sys.exit(1)

m_imported = import_module(sys.argv[1])

if m_imported.__doc__ is None:
    print("No module documentation", end="")
else:
    print("OK", end="")


# tests/conftest.py

import sys
import os

# Dynamically add the 'src' directory to Python's import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

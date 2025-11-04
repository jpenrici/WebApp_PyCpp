# -*- coding: utf-8 -*-

import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, root)
  
try:
    from cpp.lib.py_bind.adapter import count_permutations
except ImportError:
    raise ImportError("Python adapter for the C++ library not found!")


def compute_permutations(numbers):
    count, elapsed = count_permutations(numbers)
    return count, elapsed
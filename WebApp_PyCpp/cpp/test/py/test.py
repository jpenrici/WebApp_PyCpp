# -*- coding: utf-8 -*-

import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, root)
  
try:
    from lib.py_bind.adapter import count_permutations
except ImportError:
    raise ImportError("Python adapter for the C++ library not found!")


def test():
    numbers = [5, 1, 4, 2, 3]
    count, elapsed = count_permutations(numbers)

    print(f"Input numbers    : {numbers}")
    print(f"Permutation count: {count}")
    print(f"Execution time   : {elapsed:.4f} ms")


if __name__ == "__main__":
    test()

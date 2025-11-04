"""
adapter.py
-----------

Functional adapter module for the C++ shared library (libalgorithm.so).

This file loads the C++ library using ctypes, defines Python bindings for
its exported symbols, and exposes high-level Python functions ready for
direct use by Django or standalone scripts.
"""

import ctypes
import os
from typing import List, Tuple


# 1. Load the shared library
def _load_library() -> ctypes.CDLL:
    """
    Loads the compiled C++ shared library (libalgorithm.so)
    from the ../lib/ directory relative to this file.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    lib_path = os.path.join(base_dir, "libalgorithm.so")

    if not os.path.exists(lib_path):
        raise FileNotFoundError(f"Shared library not found: {lib_path}")

    # Load shared object
    return ctypes.CDLL(lib_path)


# Load once at import
_lib = _load_library()

# 2. Define function signatures
# C++ signature:
# long long count_permutations(const int* data, int length, double* duration_out);
_lib.count_permutations.argtypes = [
    ctypes.POINTER(ctypes.c_int),  # data
    ctypes.c_int,  # length
    ctypes.POINTER(ctypes.c_double),  # duration_out
]
_lib.count_permutations.restype = ctypes.c_longlong


# 3. Python-friendly wrapper
def count_permutations(data: List[int]) -> Tuple[int, float]:
    """
    Calculates the number of unique permutations of the given integer list
    using the optimized C++ backend.

    Args:
        data (List[int]): Input sequence of integers.

    Returns:
        Tuple[int, float]: A tuple containing:
            - total number of permutations
            - elapsed time in milliseconds
    """
    if not data:
        return 0, 0.0

    # Convert Python list to C array
    array_type = ctypes.c_int * len(data)
    c_array = array_type(*data)
    duration = ctypes.c_double(0.0)

    # Call the C++ function
    result = _lib.count_permutations(c_array, len(data), ctypes.byref(duration))

    return result, duration.value


# 4. Standalone usage
if __name__ == "__main__":
    test_data = [1, 2, 3, 4]
    count, elapsed = count_permutations(test_data)

    print(f"Permutation count: {count}")
    print(f"Execution time: {elapsed:.4f} ms")

# -*- coding: utf-8 -*-

import ctypes
import os
import time

LIB_NAME = "libalgorithm.so"
LIB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../../lib/{LIB_NAME}"))

if not os.path.exists(LIB_PATH):
    raise FileNotFoundError(f"Shared library not found: {LIB_PATH}")

lib = ctypes.CDLL(LIB_PATH)
lib.count_permutations.argtypes = [
    ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.POINTER(ctypes.c_double)
]
lib.count_permutations.restype = ctypes.c_longlong


def test():
    numbers = [5, 1, 4, 2, 3]
    arr = (ctypes.c_int * len(numbers))(*numbers)
    duration = ctypes.c_double()

    print(f"[PYTHON] Calling C++ library at: {LIB_PATH}")
    start_py = time.perf_counter()
    result = lib.count_permutations(arr, len(numbers), ctypes.byref(duration))
    end_py = time.perf_counter()

    print(f"Input numbers     : {numbers}")
    print(f"C++ result count  : {result}")
    print(f"C++ elapsed (ms)  : {duration.value:.3f}")
    print(f"Python overhead   : {(end_py - start_py) * 1000:.3f} ms")


if __name__ == "__main__":
    test()

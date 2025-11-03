import ctypes
import os

LIB_NAME = "libalgorithm.so"
LIB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../../cpp/lib/{LIB_NAME}"))

if not os.path.exists(LIB_PATH):
    raise FileNotFoundError(f"Shared library not found: {LIB_PATH}")

lib = ctypes.CDLL(LIB_PATH)

lib = ctypes.CDLL(LIB_PATH)
lib.count_permutations.argtypes = [
    ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.POINTER(ctypes.c_double)
]
lib.count_permutations.restype = ctypes.c_longlong


def compute_permutations(numbers):
    """
    Calls the C++ function count_permutations using ctypes.
    """
    arr = (ctypes.c_int * len(numbers))(*numbers)
    duration = ctypes.c_double()
    result = lib.count_permutations(arr, len(numbers), ctypes.byref(duration))
    return result, duration.value

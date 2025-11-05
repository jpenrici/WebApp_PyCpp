# WebApp_PyCpp

A minimal **web-based computational project** that integrates **Django (Python)** with a **C++ backend** for high-performance numerical processing.

The system demonstrates how to expose native C++ algorithms to Python through **ctypes**, wrapped inside a clean adapter module.  
The Django web interface acts as a lightweight frontend and API gateway.

---

## Project Structure

```

WebApp_PyCpp/
├── cpp/
│   ├── CMakeLists.txt
│   ├── include/
│   │   └── algorithm.hpp
│   ├── src/
│   │   └── algorithm.cpp
│   ├── lib/
│   │   ├── libalgorithm.so
│   │   └── py_bind
│   │       ├── adapter.py
│   │       └── __init__.py
│   └── test/
│       ├── cpp/
│       │   └── test.cpp
│       └── py/
│           └── test.py
└── django
    ├── calc/
    │   ├── ...
    │   ├── cpp_bridge.py
    │   ├── forms.py
    │   ├── templates/
    │   │   └── calc/
    │   │       ├── index.html
    │   │       └── result.html
    │   └── ...
    └── webapp
        └── ...

````

---

## Overview

- **C++ Module (`cpp/`)**  
  Implements the core permutation-counting algorithm using `std::next_permutation`.  
  Built as a shared library (`libalgorithm.so`) using CMake.

- **Python Adapter (`adapter.py`)**  
  Bridges the C++ library and provides a clean Python interface for use in Django or standalone scripts.

- **Django App (`django/`)**  
  Provides the web UI and form handling for user interaction and result rendering.  

---

## Build & Run

### 1. Build the C++ library
```bash
cd cpp
cmake -B build
cmake --build build
````

The library will be generated at:

```
cpp/lib/libalgorithm.so
```

### 2. Test the Python adapter

```bash
cd cpp/test/py
python3 test.py
```

Expected output:

```
Input numbers    : [5, 1, 4, 2, 3]
Permutation count: 120
Execution time   : 0.1523 ms
```

### 3. Run the Django frontend

```bash
cd django
python3 manage.py runserver
```

Then open your browser at:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Concept

* Demonstrates **cross-language integration** (C++ ⇄ Python ⇄ Web).
* Clean **adapter pattern** hides ctypes complexity.
* C++ layer can be easily replaced or extended with more algorithms.

---

## License

MIT License — feel free to use, modify, and expand this example.

---

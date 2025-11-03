cmake_minimum_required(VERSION 3.25 FATAL_ERROR)

project(Algorithm LANGUAGES CXX)

# ========== Configuration ==========

set(PROGRAM_NAME algorithm)
set(LIBRARY_NAME algorithm)

set(CMAKE_CXX_STANDARD 26)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include_directories(include)

# ========== Core Library ==========
add_library(${LIBRARY_NAME} SHARED
  src/algorithm.cpp
)

set_target_properties(${LIBRARY_NAME} PROPERTIES
    OUTPUT_NAME ${LIBRARY_NAME}
    LIBRARY_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/lib"
    ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/lib"
)

# ========== Cpp Test ==========
add_executable(${PROGRAM_NAME}_test test/cpp/test.cpp)

target_link_libraries(${PROGRAM_NAME}_test ${LIBRARY_NAME})

set_target_properties(${PROGRAM_NAME}_test PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/test/cpp
)

add_custom_target(run_cpp_test
    COMMAND ${CMAKE_BINARY_DIR}/test/cpp/${PROGRAM_NAME}_test
    DEPENDS ${PROGRAM_NAME}_test
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    COMMENT ">>> Running native C++ test ..."
)

# ========== Python Test ==========
option(BUILD_PYTHON_BINDINGS "Build Python shared library for ctypes or pybind11" ON)

set(PY_TEST_FILE "${PROJECT_SOURCE_DIR}/test/py/test.py")

find_package(Python3 COMPONENTS Interpreter REQUIRED)

add_custom_target(run_py_test
    COMMAND ${Python3_EXECUTABLE} ${PY_TEST_FILE}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/test/py
    ENVIRONMENT
        "LD_LIBRARY_PATH=${PROJECT_SOURCE_DIR}/lib:$ENV{LD_LIBRARY_PATH}"
    COMMENT ">>> Running Python ctypes test ..."
    VERBATIM
)

# ========== Utility Targets ==========
add_custom_target(run_all_tests
    COMMENT ">>> Running all tests (C++ and Python) ..."
    DEPENDS run_cpp_test run_py_test
)

# ========== Default Build Type ==========
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug CACHE STRING "Choose the build type" FORCE)
endif()

# ========== Custom Clean Target ==========
add_custom_target(deep_clean
    COMMAND ${CMAKE_COMMAND} -E remove_directory ${CMAKE_BINARY_DIR}
    COMMENT ">>> Completely cleaning the build directory: ${CMAKE_BINARY_DIR}"
)

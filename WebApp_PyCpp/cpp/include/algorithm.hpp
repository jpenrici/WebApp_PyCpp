#pragma once

#include <vector>
#include <tuple>

namespace Calc {

/**
 * @brief Calculates all permutations of a given vector and measures elapsed time.
 *
 * @param data Vector of integers.
 * @return Tuple {count, duration_ms}.
 *
 * @note Internal C++ API used by both native and external bindings.
 */
auto count_permutations(const std::vector<int>& data) -> std::tuple<long long, double>;

}

extern "C" {

/**
 * @brief Calculates the number of permutations of a given integer array.
 * Also returns the computation time in milliseconds.
 *
 * @param data Pointer to an integer array.
 * @param length Number of elements in the array.
 * @param duration_out Pointer to a double that receives the elapsed time (ms).
 * @return Total number of permutations.
 */
long long count_permutations(const int* data, int length, double* duration_out);

}

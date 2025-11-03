#include "algorithm.hpp"

#include <algorithm>
#include <chrono>

auto Calc::count_permutations(const std::vector<int> &data)
    -> std::tuple<long long, double> {

  // Time now
  auto start = std::chrono::high_resolution_clock::now();

  std::vector<int> nums{data};
  std::sort(nums.begin(), nums.end());

  long long count = 0;
  do {
    ++count;
  } while (std::next_permutation(nums.begin(), nums.end()));

  // Elapsed time
  auto end = std::chrono::high_resolution_clock::now();

  // Duration (Difference)
  std::chrono::duration<double, std::milli> duration = end - start;

  // Tuple
  return {count, duration.count()};
}

extern "C" {

long long count_permutations(const int *data, int length,
                             double *duration_out) {

  std::vector<int> nums(data, data + length);

  auto [count, duration] = Calc::count_permutations(nums);
  *duration_out = duration;

  return count;
}
}

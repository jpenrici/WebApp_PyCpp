#include "algorithm.hpp"

#include <print>

auto main() -> int {

  int data[] = {5, 1, 4, 2, 3};
  int size = 5;

  double duration = 0.0;

  long long result = count_permutations(data, size, &duration);

  std::println("Data: {}", data);
  std::println("Permutation count: {}", result); // !5 = 120
  std::println("Execution time: {} ms", duration);

  return 0;
}

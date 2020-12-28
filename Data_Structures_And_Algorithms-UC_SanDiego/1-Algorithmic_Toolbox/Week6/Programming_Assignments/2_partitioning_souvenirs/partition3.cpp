#include <iostream>
#include <vector>

int partition3(std::vector<int> &A) {
  return 1;
}

int main() {
  int n;
  std::cin >> n;
  std::vector<int> A(n);
  for (size_t i = 0; i < A.size(); ++i) {
    std::cin >> A[i];
  }
  std::cout << partition3(A) << '\n';
}

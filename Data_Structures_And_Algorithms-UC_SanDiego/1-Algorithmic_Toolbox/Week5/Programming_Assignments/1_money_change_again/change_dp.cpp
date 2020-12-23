#include <iostream>
#include <limits>
#include <vector>

int get_change(int m) {
  int element = std::numeric_limits<int>::max();
  std::vector<int> coins {1, 3, 4};
  std::vector<int> minCoins {};
  int sumCoins = 0;
  for (int i=1; i!=m+2; i++){
    minCoins.push_back(element);
  }
  minCoins[0] = 0;
  for (int i=1; i!=m+1; i++){
    for (auto el:coins){
      if (i>=el){
        sumCoins = minCoins[i-el] + 1;
        if (sumCoins<minCoins[i]){
          minCoins[i] = sumCoins;
        }
      }
    }
  }
  return minCoins[m];
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
  return 0;
}

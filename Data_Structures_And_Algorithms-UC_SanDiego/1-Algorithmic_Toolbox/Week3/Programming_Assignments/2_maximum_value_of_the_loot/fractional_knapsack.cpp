#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using std::vector;

// struct greater
// {
//   template<class T>
//   bool operator()(T const &a, T const &b) const { return a>b; }
// };

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  std::vector<double> value_per_weight;
  std::map<double, int> hashT;
  for (int i=0; i!=weights.size(); i++){
    value_per_weight.push_back(values[i]/weights[i]);
    hashT[value_per_weight[i]] = weights[i];
  }
  sort(value_per_weight.rbegin(), value_per_weight.rend(), std::greater<double>());
  // for (auto el:value_per_weight){
  //   std::cout << el << std::endl;
  //   std::cout << hashT[el] << std::endl;
  // }
  double value = 0.0;
  int alpha;
  for (int i=0; i!=value_per_weight.size(); i++){
    if (capacity==0) { return value; }
    if (capacity<hashT[value_per_weight[i]]) { alpha = capacity; }
    else { alpha = hashT[value_per_weight[i]]; }
    value += alpha*value_per_weight[i];
    capacity -= alpha;
  }
  return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(4);
  std::cout << optimal_value << std::endl;
  return 0;
}

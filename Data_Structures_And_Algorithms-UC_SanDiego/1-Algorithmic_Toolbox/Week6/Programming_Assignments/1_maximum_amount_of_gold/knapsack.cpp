#include <iostream>
#include <vector>


int optimal_weight(int W, const std::vector<int> &w) {
  int len = w.size();
  std::vector<std::vector<int>> res {};
  std::vector<int> tmpVec {};
  int newW;
  for(int i=0; i!=W+1; i++){
    tmpVec.push_back(0);
  }
  for(int i=0; i!=len+1; i++){
    res.push_back(tmpVec);
  }
  for(int i=1; i!=len+1; i++){
    for(int j=1; j!=W+1; j++){
      res[i][j] = res[i-1][j];
      if (j>=w[i-1]){
        newW = res[i - 1][j - w[i - 1]] + w[i - 1];
        if (newW > res[i][j]){
          res[i][j] = newW;
        }
      }
    }
  }
  return res[len][W];
}

int main() {
  int n, W;
  std::cin >> W >> n;
  std::vector<int> w(n);
  for (int i = 0; i < n; i++) {
    std::cin >> w[i];
  }
  std::cout << optimal_weight(W, w) << '\n';
}

#include <iostream>
#include <string>
#include <vector>
#include <limits>

int minNumber(int el1, int el2, int el3){
  int minEl = std::numeric_limits<int>::min();
  if (el1<=el2 && el1<=el3){
    minEl = el1;
  }
  if (el2<=el1 && el2<=el3){
    minEl = el2;
  }
  if (el3<=el1 && el3<=el2){
    minEl = el3;
  }
  return minEl;
}

int edit_distance(const std::string &str1, const std::string &str2) {
  int element = std::numeric_limits<int>::min();
  int distance = 0;
  std::vector<int> tmpVec {};
  std::vector<std::vector<int>> D {};
  for (int i=0; i!=str2.length()+1; i++){
    tmpVec.push_back(element);
  }
  for (int i=0; i!=str1.length()+1; i++){
    D.push_back(tmpVec);
  }
  for (int i=0; i!=str1.length()+1; i++){
    D[i][0] = i;
  }
  for (int i=0; i!=str2.length()+1; i++){
    D[0][i] = i;
  }
  for (int i=1; i!=str1.length()+1; i++){
    for (int j=1; j!=str2.length()+1; j++){
      if (str1[i-1] == str2[j-1]){ distance = 0; }
      else { distance = 1; }
      D[i][j] = minNumber(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+distance);
    }
  }
  return D[str1.length()][str2.length()];
}

int main() {
  std::string str1;
  std::string str2;
  std::cin >> str1 >> str2;
  std::cout << edit_distance(str1, str2) << std::endl;
  return 0;
}

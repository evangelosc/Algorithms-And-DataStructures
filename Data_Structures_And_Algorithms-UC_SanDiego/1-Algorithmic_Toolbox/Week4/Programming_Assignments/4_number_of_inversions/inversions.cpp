#include <iostream>
#include <vector>

int merge(std::vector<int> a, std::vector<int> tmp_a, int left, int m, int right){
  int i = left;
  int j = m + 1;
  int k = left;
  int inversions = 0;
  while (i<=m && j<=right){
    if (a[i]<=a[j]){
      tmp_a[k] = a[i];
      k++;
      i++;
    } else {
      inversions += (m-i+1);
      tmp_a[k] = a[j];
      k++;
      j++;
    }
  }
  while (i<=m){
    tmp_a[k] = a[i];
    k++;
    i++;
  }
  while (j<=right){
    tmp_a[k] = a[j];
    k++;
    j++;
  }
  for (int i=left; i!=right+1; i++){a[i]=tmp_a[i];}
  return inversions;
}

int _mergeSort(std::vector<int> a, std::vector<int> tmp_a, int left, int right){
  int inversions = 0;
  if (left<right){
    int m = (int)((left+right)/2);
    inversions += _mergeSort(a, tmp_a, left, m);
    inversions += _mergeSort(a, tmp_a, m+1, right);
    inversions += merge(a, tmp_a, left, m, right);
  }
  return inversions;
}

int mergeSort(std::vector<int> a, int n){
  std::vector<int> tmp_a;
  for (int i=0; i!=n; i++){
    tmp_a.push_back(0);
  }
  // for (auto el:tmp_a) {std::cout << el << std::endl;}
  return _mergeSort(a, tmp_a, 0, n-1);
}


int main() {
  int n;
  std::cin >> n;
  std::vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  std::vector<int> b(a.size());
  std::cout << mergeSort(a, a.size()) << '\n';
}

#include <algorithm>
#include <iostream>
#include <vector>
#include <tuple>

std::tuple<int, int> part3Fun(std::vector<int> &a, int left, int right){
  int pivot = a[right];
  int i = left - 1;
  int p = left - 1;
  int j = right;
  int q = right;
  int swap, k;

  while (true){
    while (a[i+1] < pivot){
      i++;
    }
    i++;
    while (a[j-1] > pivot){
      j--;
    }
    j--;
    if (i >= j){break;}
    swap = a[i];
    a[i] = a[j];
    a[j] = swap;
    if (a[i]==pivot){
      p++;
      swap = a[i];
      a[i] = a[p];
      a[p] = swap;
    }
    if (a[j]==pivot){
      q--;
      swap = a[j];
      a[j] = a[q];
      a[q] = swap;
    }
  }
  swap = a[i];
  a[i] = a[right];
  a[right] = swap;

  j = i - 1;
  k = left;
  while (k<=p){
    swap = a[k];
    a[k] = a[j];
    a[j] = swap;
    j--;
    k++;
  }
  i++;
  k = right - 1;
  while (k>=q){
    swap = a[k];
    a[k] = a[i];
    a[i] = swap;
    i++;
    k--;
  }
  return std::make_tuple(j, i);
}

void quicksort3(std::vector<int> &a, int left, int right){
  if (right<=left){return;}
  int j, i;
  std::tie(j, i) = part3Fun(a, left, right);
  quicksort3(a, left, j);
  quicksort3(a, i, right);
}

int majority_element(std::vector<int> &a, int number){
  int i = 0;
  int count;
  while (i<number){
    count = 1;
    while (i<number-1 && a[i+1]==a[i]){
      count++;
      i++;
    }
    if (count > (int)number/2){return 1;}
    i++;
  }
  return 0;
}

int main() {
  int n;
  std::cin >> n;
  std::vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  quicksort3(a, 0, a.size());
  std::cout << majority_element(a, a.size()) << '\n';
}

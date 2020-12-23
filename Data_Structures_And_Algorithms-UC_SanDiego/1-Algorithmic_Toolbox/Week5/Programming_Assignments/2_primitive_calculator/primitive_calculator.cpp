#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <tuple>

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

std::tuple<std::vector<int>, std::vector<int>> optimal_operations(int n) {
  std::vector<int> sequence {};
  std::vector<int> lastSequence {};
  int n3 = 0;
  int n2 = 0;
  int element = std::numeric_limits<int>::max();
  for (int i=0; i!=2; i++){sequence.push_back(0);}
  for (int i=2; i!=n+2; i++){
    sequence.push_back(element);
  }
  for (int i=0; i!=n+2; i++){
    lastSequence.push_back(0);
  }
  for (int i=2; i!=n+1; i++){
    if (i%3!=0){
      n3 = element;
    } else {
      n3 = sequence[(int)(i/3)];
    }
    if (i%2!=0){
      n2 = element;
    } else {
      n2 = sequence[(int)(i/2)];
    }
    sequence[i] = minNumber(sequence[i-1], n2, n3) + 1;
    if (sequence[i] == n3 + 1){
      lastSequence[i] = (int)(i/3);
    }
    if (sequence[i] == n2 + 1){
      lastSequence[i] = (int)(i/2);
    }
    if (sequence[i] == sequence[i-1]+1){
      lastSequence[i] = i-1;
    }
  }
  return std::make_tuple(sequence, lastSequence);
}

std::vector<int> optimal_sequence(std::vector<int> lastSequence, int n){
  std::vector<int> seq {};
  seq.push_back(n);
  int i = n;
  int lastNumber = 0;
  while (i>1){
    lastNumber = lastSequence[i];
    seq.push_back(lastNumber);
    i = lastNumber;
  }
  sort(seq.begin(), seq.end());
  return seq;
}

int main() {
  int n;
  std::cin >> n;
  std::vector<int> sequence {};
  std::vector<int> lastSequence {};
  std::tie(sequence, lastSequence) = optimal_operations(n);
  std::vector<int> seq = optimal_sequence(lastSequence, n);
  std::cout << sequence[n] << std::endl;
  for (size_t i = 0; i < seq.size(); ++i) {
    std::cout << seq[i] << " ";
  }
  return 0;
}

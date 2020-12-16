#include <iostream>

int get_change(int m) {
  int n = 0;
  while (m>0){
    if ((int)m/10!=0) {
      n++;
      m -= 10;
    } else if ((int)m/5!=0){
      n++;
      m -= 5;
    } else {
      n++;
      m -= 1;
    }
  }
  return n;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}

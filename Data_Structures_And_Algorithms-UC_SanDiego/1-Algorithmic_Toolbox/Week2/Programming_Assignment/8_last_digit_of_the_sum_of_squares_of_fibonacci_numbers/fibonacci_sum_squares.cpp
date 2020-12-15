#include <iostream>
#include <vector>
#include <string>

int fibonacci_sum_squares(long long n) {
    std::vector<int> f {0, 1};
    std::vector<int> last {0, 1};
    std::string tmp;
    for (int i=2; i!=60; ++i){
        f.push_back(f[i-1]+f[i-2]);
        tmp = std::to_string(f[i]).back();
        last.push_back(std::stoi(tmp));
    }
    int res = last[n%60]*last[n%60] + last[n%60]*last[(n-1)%60];
    return res%10;
}

int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_squares(n);
}

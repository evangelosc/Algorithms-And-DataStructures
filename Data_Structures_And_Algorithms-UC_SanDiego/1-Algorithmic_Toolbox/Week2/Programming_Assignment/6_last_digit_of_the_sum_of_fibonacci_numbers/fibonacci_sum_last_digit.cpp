#include <iostream>
#include <vector>
#include <string>

int fibonacci_sum(long long n) {
    std::vector<int> f {0, 1};
    std::vector<int> last {0, 1};
    std::string tmp;
    for (int i=2; i!=60; ++i){
        f.push_back(f[i-1]+f[i-2]);
        tmp = std::to_string(f[i]).back();
        last.push_back(std::stoi(tmp));
    }
    // # Sn = 2 * F[n] + F[n-1] - 1
    int res = (int)2*last[n%60] + last[(n-1)%60] - 1;
    return (int)res%10;
}

int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum(n);
}

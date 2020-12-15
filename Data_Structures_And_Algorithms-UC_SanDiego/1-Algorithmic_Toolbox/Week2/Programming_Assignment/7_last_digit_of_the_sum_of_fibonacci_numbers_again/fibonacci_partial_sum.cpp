#include <iostream>
#include <vector>
using std::vector;

long long get_fibonacci_partial_sum(long long m, long long n) {
    std::vector<int> f {0, 1};
    std::vector<int> last {0, 1};
    std::string tmp;
    for (int i=2; i!=60; ++i){
        f.push_back(f[i-1]+f[i-2]);
        tmp = std::to_string(f[i]).back();
        last.push_back(std::stoi(tmp));
    }
    int q = (int)((n-m+1)/60);
    long long total = 0;
    for (long long i=(m+(q*60)); i!=(n+1); i++){
        total = (long long) (total + last[i%60]);
    }
    return (long long)total%10;
}

int main() {
    long long from, to;
    std::cin >> from;
    std::cin >> to;
    std::cout << get_fibonacci_partial_sum(from, to) << '\n';
}

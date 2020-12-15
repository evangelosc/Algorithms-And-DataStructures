#include <iostream>

int pisanoPeriod(int m){
    int previous = 0;
    int current = 1;
    for(int i=0; i!=m*m; i++){
        previous = current;
        current = (int)(previous+current)%m;
        if (previous==0 and current==1){
            return i+1;
        }
    }
}

long long get_fibonacci_huge(long long n, long long m) {
    if (n <= 1)
        return n;
    n = (long long)n%pisanoPeriod(m);
    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < (n - 1); ++i) {
        std::cout << current << std::endl;
        previous = current;
        current = previous + current;
    }

    return current % m;
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonacci_huge(n, m) << '\n';
}

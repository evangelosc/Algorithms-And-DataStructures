#include <iostream>

int get_fibonacci_last_digit(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 2; i < n; ++i) {
        previous = current;
        current = previous + current;
        previous %= 10;
        current %= 10;
    }

    return current;
}

int main() {
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit(n);
    std::cout << c << '\n';
}

#include <climits>
#include <iostream>

class Solution {
public:
    int reverse(int x) {
        long res = 0;
        do {
            res = res*10 + x%10;
        } while (x /= 10);
        return res>INT_MAX ? 0 : res;
    }
};


int main()
{
    Solution s;
    std::cout << s.reverse(123) << std::endl;
    std::cout << s.reverse(-123) << std::endl;
    std::cout << s.reverse(10100) << std::endl;
    std::cout << s.reverse(1000000003) << std::endl;

    return 0;
}
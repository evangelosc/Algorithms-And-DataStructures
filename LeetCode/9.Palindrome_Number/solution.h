#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        int given = x;
        int dig;
        double rev;
        while(x>0){
            dig = x%10;
            rev = rev*10 + dig;
            x /= 10;
            x = (int)x;
        }
        if (rev==given) { return true; }
        return false;
    }
};
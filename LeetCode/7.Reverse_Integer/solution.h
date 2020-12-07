#include <iostream>
#include <math.h>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        bool negative_flag = false;
        if (x<0) { negative_flag = true;}
        x = abs(x);
        long int reversed = 0;
        while (x>0){
            reversed *= 10;
            reversed += x%10;
            x /= 10;
            x = (int)x;
        }
        int INT_MAX_32 = pow(2, 31)-1;
        if (reversed>INT_MAX_32){ return 0; }
        else if (negative_flag) { return -reversed; }
        else { return reversed; }
    }
};
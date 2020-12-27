#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool judgeCircle(string moves) {
        int y_prime = 0;
        int x_prime = 0;
        for (auto el:moves){
            if (el=='U') { y_prime++; }
            if (el=='D') { y_prime--; }
            if (el=='R') { x_prime++; }
            if (el=='L') { x_prime--; }
        }
        if (x_prime==0 && y_prime==0) { return true; }
        return false;
    }
};
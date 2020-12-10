#include "solution.h"

// Unit Test

int main(){
    Solution s;
    int t1 = 4;
    int t2 = 8;
    if (s.mySqrt(t1) == 2) { cout << "Pass" << endl;}
    else { cout << "Failed 1 - t1" << endl;}
    if (s.mySqrt(t2) == 2) { cout << "Pass" << endl;}
    else { cout << "Failed 2 - t2" << endl;}
    return 0;
}
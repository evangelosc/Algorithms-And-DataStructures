#include "solution.h"

// Unit Test

int main(){
    Solution s;
    int t1 = 2;
    int t2 = 3;
    if (s.climbStairs(t1) == 2) { cout << "Pass" << endl;}
    else { cout << "Failed 1 - t1" << endl;}
    if (s.climbStairs(t2) == 3) { cout << "Pass" << endl;}
    else { cout << "Failed 2 - t2" << endl;}
    return 0;
}
#include "solution.h"

// Unit Test

int main(){
    Solution s;
    int n = 5;
    int start = 0;
    if (s.xorOperation(n, start)==8) {cout << "PASS" << endl;}
    else {cout << "Test Failed" << endl;}
    return 0;
}
#include "solution.h"

// Unit Test

int main(){
    Solution s;
    int t1 = 1;
    int t2 = 4;
    if (s.countAndSay(t1) == "1") { cout << "Pass" << endl;}
    else { cout << "Failed 1 - t1" << endl;}
    if (s.countAndSay(t2) == "1211") { cout << "Pass" << endl;}
    else { cout << "Failed 2 - t2" << endl;}
    return 0;
}
#include "solution.h"

// Unit Test

int main(){
    Solution s;
    if (s.canWinNim(1) == true) { cout << "Test 1 - PASS" << endl;}
    else { cout << "Test 1 - Failed" << endl; }
    if (s.canWinNim(2) == true) { cout << "Test 2 - PASS" << endl;}
    else { cout << "Test 2 - Failed" << endl; }
    return 0;
}
#include "solution.h"

// Unit Test

int main(){
    Solution s;
    if (s.numberOfMatches(7) == 6) { cout << "PASS" << endl;}
    else { cout << "Test Failed" << endl; }
    if (s.numberOfMatches(14) == 13) { cout << "PASS" << endl;}
    else { cout << "Test Failed" << endl; }
    return 0;
}
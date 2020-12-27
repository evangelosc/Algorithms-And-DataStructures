#include "solution.h"

// Unit Test

int main(){
    Solution s;
    string string1 = "UD";
    string string2 = "LL";
    
    if (s.judgeCircle(string1) == true) { cout << "Test 1 - PASS" << endl;}
    else { cout << "Test 1 - Failed" << endl; }
    if (s.judgeCircle(string2) == false) { cout << "Test 2 - PASS" << endl;}
    else { cout << "Test 2 - Failed" << endl; }
    return 0;
}
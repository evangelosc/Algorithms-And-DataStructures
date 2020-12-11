#include "solution.h"

// Unit Test

int main(){
    Solution s;
    string string1 = "A man, a plan, a canal: Panama";
    string string2 = "race a car";
    
    if (s.isPalindrome(string1) == true) { cout << "Test 1 - PASS" << endl;}
    else { cout << "Test 1 - Failed" << endl; }
    if (s.isPalindrome(string2) == false) { cout << "Test 2 - PASS" << endl;}
    else { cout << "Test 2 - Failed" << endl; }
    return 0;
}
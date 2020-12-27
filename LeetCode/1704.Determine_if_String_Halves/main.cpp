#include "solution.h"

// Unit Test

int main(){
    Solution s;
    string s1 = "book";
    string s2 = "textbook";
    string s3 = "MerryChristmas";
    if (s.halvesAreAlike(s1)==true) { cout << "Test 1 Pass" << endl;}
    else { cout << "Test 1 failed" << endl;}
    if (s.halvesAreAlike(s2)==false) { cout << "Test 2 Pass" << endl;}
    else { cout << "Test 2 failed" << endl;}
    if (s.halvesAreAlike(s3)==false) { cout << "Test 3 Pass" << endl;}
    else { cout << "Test 3 failed" << endl;}
    return 0;
}
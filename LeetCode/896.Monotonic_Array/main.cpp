#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {1,2,2,3};
    vector<int> v2 {6,5,4,4};
    vector<int> v3 {1,3,2};
    vector<int> v4 {1,2,4,5};
    vector<int> v5 {1,1,1};
    
    if (s.isMonotonic(v1) == true) { cout << "Test 1 - PASS" << endl;}
    else { cout << "Test 1 - Failed" << endl; }
    if (s.isMonotonic(v2) == true) { cout << "Test 2 - PASS" << endl;}
    else { cout << "Test 2 - Failed" << endl; }
    if (s.isMonotonic(v3) == false) { cout << "Test 3 - PASS" << endl;}
    else { cout << "Test 3 - Failed" << endl; }
    if (s.isMonotonic(v4) == true) { cout << "Test 4 - PASS" << endl;}
    else { cout << "Test 4 - Failed" << endl; }
    if (s.isMonotonic(v5) == false) { cout << "Test 5 - PASS" << endl;}
    else { cout << "Test 5 - Failed" << endl; }
    return 0;
}
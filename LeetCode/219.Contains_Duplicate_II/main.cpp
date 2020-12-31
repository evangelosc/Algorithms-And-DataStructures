#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {1,2,3,1};
    vector<int> v2 {1,0,1,1};
    vector<int> v3 {1,2,3,1,2,3};

    
    if (s.containsNearbyDuplicate(v1, 3) == true) { cout << "Test 1 - PASS" << endl;}
    else { cout << "Test 1 - Failed" << endl; }
    if (s.containsNearbyDuplicate(v2, 1) == true) { cout << "Test 2 - PASS" << endl;}
    else { cout << "Test 2 - Failed" << endl; }
    if (s.containsNearbyDuplicate(v3, 2) == false) { cout << "Test 3 - PASS" << endl;}
    else { cout << "Test 3 - Failed" << endl; }
    return 0;
}
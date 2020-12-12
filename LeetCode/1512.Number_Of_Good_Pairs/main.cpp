#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {1,2,3,1,1,3};
    vector<int> v2 {1,1,1,1};
    vector<int> v3 {1,2,3};
    if (s.numIdenticalPairs(v1) == 4) {cout << "Pass" << endl; } else {cout << "Failed 1" << endl; }
    if (s.numIdenticalPairs(v2) == 6) {cout << "Pass" << endl; } else {cout << "Failed 2" << endl; }
    if (s.numIdenticalPairs(v3) == 0) {cout << "Pass" << endl; } else {cout << "Failed 3" << endl; }
    
    return 0;
}
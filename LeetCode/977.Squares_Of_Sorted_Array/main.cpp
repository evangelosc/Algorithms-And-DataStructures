#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {-4,-1,0,3,10};
    vector<int> v2 {-7,-3,2,3,11};
    vector<int> res_v1 {0,1,9,16,100};
    vector<int> res_v2 {4,9,9,49,121};

    if (s.sortedSquares(v1) == res_v1) { cout << "Test 1 - PASS" << endl;}
    else { cout << "Test 1 - Failed" << endl; }
    if (s.sortedSquares(v2) == res_v2) { cout << "Test 2 - PASS" << endl;}
    else { cout << "Test 2 - Failed" << endl; }
    return 0;
}
#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {1,1,2};
    vector<int> v2 {0,0,1,1,1,2,2,3,3,4};
    if (s.removeDuplicates(v1) == 2) { cout << "Pass" << endl;}
    else { cout << "Failed - v1" << endl;}
    if (s.removeDuplicates(v2) == 5) { cout << "Pass" << endl;}
    else { cout << "Failed - v2" << endl;}
    return 0;
}

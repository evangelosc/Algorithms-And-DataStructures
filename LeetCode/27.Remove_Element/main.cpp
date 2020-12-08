#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {3,2,2,3};
    int val1 = 3;
    vector<int> v2 {0,1,2,2,3,0,4,2};
    int val2 = 2;
    if (s.removeElement(v1, val1) == 2) { cout << "Pass" << endl;}
    else { cout << "Failed - v1" << endl;}
    if (s.removeElement(v2, val2) == 5) { cout << "Pass" << endl;}
    else { cout << "Failed - v2" << endl;}
    return 0;
}
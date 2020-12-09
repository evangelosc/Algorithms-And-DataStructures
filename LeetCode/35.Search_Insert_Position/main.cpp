#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {1,3,5,6};
    int t1 = 5;
    int t2 = 2;
    int t3 = 7;
    vector<int> vextra {1};
    int textra = 0;
    cout << "First Function Test Start" << endl;
    if (s.searchInsert(v1, t1) == 2) { cout << "Pass" << endl;}
    else { cout << "Failed 1 - v1 t1" << endl;}
    if (s.searchInsert(v1, t2) == 1) { cout << "Pass" << endl;}
    else { cout << "Failed 2 - v1 t2" << endl;}
    if (s.searchInsert(v1, t3) == 4) { cout << "Pass" << endl;}
    else { cout << "Failed 3 - v1 t3" << endl;}
    if (s.searchInsert(v1, textra) == 0) { cout << "Pass" << endl;}
    else { cout << "Failed 4 - v1 textra" << endl;}
    if (s.searchInsert(vextra, textra) == 0) { cout << "Pass" << endl;}
    else { cout << "Failed extra - vextra textra" << endl;}
    cout << "First Function Test End" << endl;
    cout << "------------------------" << endl;
    cout << "Second Function Test Start" << endl;
    if (s.searchInsert2(v1, t1) == 2) { cout << "Pass" << endl;}
    else { cout << "Second Failed 1 - v1 t1" << endl;}
    if (s.searchInsert2(v1, t2) == 1) { cout << "Pass" << endl;}
    else { cout << "Second Failed 2 - v1 t2" << endl;}
    if (s.searchInsert2(v1, t3) == 4) { cout << "Pass" << endl;}
    else { cout << "Second Failed 3 - v1 t3" << endl;}
    if (s.searchInsert2(v1, textra) == 0) { cout << "Pass" << endl;}
    else { cout << "Second Failed 4 - v1 textra" << endl;}
    if (s.searchInsert2(vextra, textra) == 0) { cout << "Pass" << endl;}
    else { cout << "Second Failed extra - vextra textra" << endl;}
    cout << "Second Function Test End" << endl;
    return 0;
}
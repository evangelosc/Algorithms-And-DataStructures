#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<string> w1 {"ab", "c"};
    vector<string> w2 {"a", "bc"};
    vector<string> w11 {"a", "cb"};
    vector<string> w22 {"ab", "c"};
    if (s.arrayStringsAreEqual(w1, w2) == true) {cout << "Pass" << endl; } else {cout << "Failed 1" << endl; }
    if (s.arrayStringsAreEqual(w11, w22) == false) {cout << "Pass" << endl; } else {cout << "Failed 2" << endl; }
    
    return 0;
}
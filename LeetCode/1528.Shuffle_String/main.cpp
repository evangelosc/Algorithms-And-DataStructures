#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {4,5,6,7,0,2,1,3};
    vector<int> v2 {0,1,2};
    vector<int> v3 {3,1,4,2,0};
    string s1 = "codeleet";
    string s2 = "abc";
    string s3 = "aiohn";
    if (s.restoreString(s1, v1) == "leetcode") {cout << "Pass" << endl; } else {cout << "Failed 1" << endl; }
    if (s.restoreString(s2, v2) == "abc") {cout << "Pass" << endl; } else {cout << "Failed 2" << endl; }
    if (s.restoreString(s3, v3) == "nihao") {cout << "Pass" << endl; } else {cout << "Failed 3" << endl; }
    
    return 0;
}
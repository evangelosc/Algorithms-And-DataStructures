#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<string> v2 {"dog","racecar","car"};
    vector<string> v1 {"flower","flow","flight"};
    auto res1 = s.longestCommonPrefix(v1);
    auto res2 = s.longestCommonPrefix(v2);
    cout << "fl == " << res1 << endl;
    cout << " == " << res2 << endl; 
    return 0;
}
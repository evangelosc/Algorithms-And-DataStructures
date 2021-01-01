#include "solution.h"

// Unit Test

int main(){
    Solution s;
    string allowed = "ab";
    vector<string> words {"ad","bd","aaab","baa","badab"};
    if (s.countConsistentStrings(allowed, words) == 2) { cout << "PASS" << endl;}
    else {cout<<"FAILED"<<endl;}
    return 0;
}
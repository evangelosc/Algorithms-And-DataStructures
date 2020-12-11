#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        if (s.length()==0) { return true; }
        string res = "";
        for (auto el:s){
            if (isalnum(el)){
                res += el;
            }
        }
        string lower_str = "";
        for (auto it=res.begin(); it!=res.end(); it++){
            lower_str += tolower(*it);
        }
        int first = 0;
        int last = lower_str.length() - 1;
        while(first<=last){
            if (lower_str[first]!=lower_str[last]) { return false; }
            first++;
            last--;
        }
        return true;
    }
};
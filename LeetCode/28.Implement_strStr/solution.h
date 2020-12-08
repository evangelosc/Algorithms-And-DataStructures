#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.length()==0) { return 0; }
        if (needle.length()>haystack.length()) { return -1; }
        int s=0, f=needle.length()-1;
        while (f<haystack.length()){
            if (haystack.substr(s, f+1-s)!=needle){ s++; }
            else { return s; }
            f++;
        }
        return -1;
    }
};
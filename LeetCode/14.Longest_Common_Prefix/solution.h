#include <iostream>
#include <string>
#include <limits>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size()==0) { return ""; }
        if (strs.size()==1) { return strs[0]; }
        int min = std::numeric_limits<int>::max();
        string prefix = "";
        string minS = "";
        for(auto el:strs){
            if (el.size()<min){
                minS = el;
                min = el.size();
            }
        }
        for (int i=0; i!=minS.size(); i++){
            for (int j=0; j!=strs.size(); j++){
                if (minS[i]==strs[j][i]){
                    continue;
                } else{ return prefix; }
            }
            prefix += minS[i];
        }
        return prefix;
    }
};
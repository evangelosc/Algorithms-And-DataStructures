#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        vector<string> finale {};
        for (int i=0; i!=indices.size(); i++){
            finale.push_back("");
        }
        for (int i=0; i!=indices.size(); i++){ finale[indices[i]] = s[i]; }
        string res = "";
        for (auto el:finale){ res+=el; }
        return res;
    }
};
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string w1 = "";
        string w2 = "";
        for (auto el:word1){ w1 += el; }
        for (auto el:word2){ w2 +=el; }
        return w1==w2;
    }
};
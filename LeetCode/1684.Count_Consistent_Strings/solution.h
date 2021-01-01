#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int count = 0;
        for (auto word:words){
            count++;
            for (auto letter:word){
                if (!inword(letter, allowed)) { count--; break;}
            }
        }
        return count;
    }
    bool inword(char letter, string word){
        for (auto el:word){
            if (el==letter) { return true; }
        }
        return false;
    }
};
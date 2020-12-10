#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int counter = 0;
        bool firstEmptyChar = true;
        for (auto it=s.rbegin(); it!=s.rend(); it++){
            if ((*it) != ' '){
                counter += 1;
                firstEmptyChar = false;
            } else {
                if (firstEmptyChar==false) { break; }
            }
        }
        return counter;
    }
};
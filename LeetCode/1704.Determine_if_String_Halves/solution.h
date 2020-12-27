#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool halvesAreAlike(string s) {
        transform(cbegin(s), cend(s), begin(s), [](const unsigned char i){ return tolower(i); });
        int pivot = (int)s.length()/2;
        if (countVowels(s.substr(0,pivot))==countVowels(s.substr(pivot,pivot))) { return true; }
        return false;
    }
    
    int countVowels(string s){
        int counter = 0;
        std::vector<char> myVec {'a', 'e', 'i', 'o', 'u'};
        for (auto el:s){
            for (auto myCase:myVec){
                if (myCase==el){counter++;}
            }
        }
        return counter;
    }
};
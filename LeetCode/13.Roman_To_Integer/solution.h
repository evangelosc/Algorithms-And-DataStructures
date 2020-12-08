#include <iostream>
#include <map>
#include <string>
using namespace std;


class Solution {
public:
    int romanToInt(string s) {
        map<char, int> roman_map;
        roman_map['I'] = 1;
        roman_map['V'] = 5;
        roman_map['X'] = 10;
        roman_map['L'] = 50;
        roman_map['C'] = 100;
        roman_map['D'] = 500;
        roman_map['M'] = 1000;
        int res = 0;
        for (int i=0; i!=s.length(); i++){
            if ((i+1<s.length())and(roman_map[s[i]]<roman_map[s[i+1]])){
                res -= roman_map[s[i]];
            } else{
                res += roman_map[s[i]];
            }
        }
        return res;
    }
};
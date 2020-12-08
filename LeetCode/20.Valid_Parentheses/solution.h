#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        if (s.length()==0) { return false; }
        if (s.length()==1) { return false; }
        for (int i=0; i!=s.length(); i++){
            if ((s[i]=='(')||(s[i]=='[')||(s[i]=='{')) { stack.push(s[i]); }
            else {
            if ((s[i]==')')&&((stack.size()==0)||(stack.top()!='('))) { return false; }
            if ((s[i]==']')&&((stack.size()==0)||(stack.top()!='['))) { return false; }
            if ((s[i]=='}')&&((stack.size()==0)||(stack.top()!='{'))) { return false; }
            stack.pop();
            }
        }
        if (stack.size()==0) { return true;}
        return false;
    }
};
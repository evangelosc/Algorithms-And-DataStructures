#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string interpret(string command) {
        string res = "";
        int index = 0;
        while (index!=command.length()){
            if (command[index]=='G') { res += "G"; }
            else if ((command[index]=='(')&&(command[index+1]==')'))
            { 
                res += "o";
                index += 1;
            }
            else { 
                res += "al";
                index += 3;
            }
            index += 1;
        }
        return res;
    }
};
#include "solution.h"

// Unit Test

int main(){
    Solution s;
    string s1 = "()";
    string s2 = "(){}[]";
    string s3 = "(]";
    string s4 = "([)]";
    cout << s.isValid(s1) << endl;
    cout << s.isValid(s2) << endl;
    cout << s.isValid(s3) << endl;
    cout << s.isValid(s4) << endl;
    return 0;
}
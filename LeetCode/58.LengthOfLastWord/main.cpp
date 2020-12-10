#include "solution.h"

// Unit Test

int main(){
    Solution s;
    string string1 = "Hello World";
    string string2 = " ";
    string string3 = " a";
    if (s.lengthOfLastWord(string1) == 5) { cout << "Pass" << endl;}
    else { cout << "Failed 1 - string1" << endl;}
    if (s.lengthOfLastWord(string2) == 0) { cout << "Pass" << endl;}
    else { cout << "Failed 2 - string2" << endl;}
    if (s.lengthOfLastWord(string3) == 1) { cout << "Pass" << endl;}
    else { cout << "Failed 3 - string3" << endl;}

    return 0;
}
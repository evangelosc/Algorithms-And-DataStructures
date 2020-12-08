#include "solution.h"

// Unit Test

int main(){
    Solution s;
    string h1 = "hello", n1 = "ll";
    string h2 = "aaaaa", n2 = "bba";
    string h3 = "", n3 = "";
    if (s.strStr(h1, n1) == 2) { cout << "Pass" << endl;}
    else { cout << "Failed - h1 n1" << endl;}
    if (s.strStr(h2, n2) == -1) { cout << "Pass" << endl;}
    else { cout << "Failed - h2 n2" << endl;}
    if (s.strStr(h3, n3) == 0) { cout << "Pass" << endl;}
    else { cout << "Failed - h3 n3" << endl;}
    return 0;
}
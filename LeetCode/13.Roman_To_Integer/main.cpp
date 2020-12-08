#include "solution.h"

// Unit Test

int main(){
    Solution s;
    if (s.romanToInt("IV") == 4) { cout << "Pass" << endl; } else { cout << "Failed - IV"; }
    if (s.romanToInt("IX") == 9)  { cout << "Pass" << endl; } else { cout << "Failed - IX"; }
    if (s.romanToInt("XL") == 40)  { cout << "Pass" << endl; } else { cout << "Failed - XL"; }
    if (s.romanToInt("XC") == 90) { cout << "Pass" << endl; } else { cout << "Failed - XC"; }
    if (s.romanToInt("CD") == 400)  { cout << "Pass" << endl; } else { cout << "Failed - CD"; }
    if (s.romanToInt("CM") == 900) { cout << "Pass" << endl; } else { cout << "Failed - CM"; }
    if (s.romanToInt("MMXIV") == 2014)  { cout << "Pass" << endl; } else { cout << "Failed - MMXIV"; }
    if (s.romanToInt("MDCCCLXXXIV") == 1884)  { cout << "Pass" << endl; } else { cout << "Failed -MDCCCLXXXIV"; }
    return 0;
}

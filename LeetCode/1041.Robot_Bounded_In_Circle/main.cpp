#include "solution.h"

// Unit Test

int main(){
    Solution s;
    string t1 = "GGLLGG";
    string t2 = "GG";
    string t3 = "GL";
    if (s.isRobotBounded(t1) == true) { cout << "Pass" << endl;}
    else { cout << "Failed 1 - t1" << endl;}
    if (s.isRobotBounded(t2) == false) { cout << "Pass" << endl;}
    else { cout << "Failed 2 - t2" << endl;}
    if (s.isRobotBounded(t3) == true) { cout << "Pass" << endl;}
    else { cout << "Failed 3 - t3" << endl;}
    return 0;
}
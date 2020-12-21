#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<vector<int>> v1 {{2,4}, {6,10}};
    cout << s.getRandom(v1) << endl;
    return 0;
}
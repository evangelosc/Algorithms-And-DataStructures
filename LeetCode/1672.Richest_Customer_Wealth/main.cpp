#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<vector<int>> accounts {{1,2,3}, {3,2,1}};
    cout << s.maximumWealth(accounts) << endl;
}
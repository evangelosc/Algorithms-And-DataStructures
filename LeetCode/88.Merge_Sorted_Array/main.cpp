#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {1,2,3,0,0,0};
    vector<int> v2 {2,5,6};
    int m = 3;
    int n = 3;
    s.merge(v1, m, v2, n);
    for (auto el:v1){ cout << el << " ";}
    cout << endl;
    return 0;
}
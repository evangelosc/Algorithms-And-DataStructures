#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {2,5,1,3,4,7};
    int n1 = 3;
    vector<int> v2 {1,2,3,4,4,3,2,1};
    int n2 = 4;
    vector<int> v3 {1,1,2,2};
    int n3 = 2;
    vector<int> res1 = s.shuffle(v1, n1);
    vector<int> res2 = s.shuffle(v2, n2);
    vector<int> res3 = s.shuffle(v3, n3);
    
    return 0;
}
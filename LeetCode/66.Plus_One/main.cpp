#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {1,2,3};
    vector<int> v2 {4,3,2,1};
    vector<int> v3 {9,9,9};
    
    vector<int> res1 = s.plusOne(v1);
    vector<int> res2 = s.plusOne(v2);
    vector<int> res3 = s.plusOne(v3);


    for (int i=0; i!=v1.size(); i++){
        if (v1[i]!=res1[i]){ cout << "Failed 1 - v1" << endl; }
    }
    for (int i=0; i!=v2.size(); i++){
        if (v2[i]!=res2[i]){ cout << "Failed 2 - v2" << endl; }
    } 
    for (int i=0; i!=v3.size(); i++){
        if (v3[i]!=res3[i]){ cout << "Failed 3 - v3" << endl; }
    }

    return 0;
}
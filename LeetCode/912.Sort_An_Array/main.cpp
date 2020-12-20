#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> v1 {5,1,1,2,0,0};
    vector<int> res_v1 {0,0,1,1,2,5};
    
    vector<int> out_v1 = s.sortArray_ms(v1);
    for(int i=0; i!=out_v1.size(); i++){
        if (out_v1[i]!=res_v1[i]) {cout << "TEST FAILED" << endl;}
    }
    return 0;
}
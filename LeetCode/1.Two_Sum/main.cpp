#include "solution.h"

// Unit Test

int main(){
    vector<int> nums {2,7,11,15};
    int target = 9;
    Solution s;
    auto res = s.twoSum(nums, target);
    for (auto el:res){
        cout << el << endl;
    }
    return 0;
}
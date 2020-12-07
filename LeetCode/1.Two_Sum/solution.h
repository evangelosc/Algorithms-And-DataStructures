#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> buff;
        for (int i=0; i!=(int)nums.size(); i++){
            if ( buff.find(nums[i]) == buff.end() ) {
                buff.insert({target-nums[i], i});
            } else {
                return {buff[nums[i]], i};
            }
        }
        return {-1, -1};
    }
};
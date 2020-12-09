#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size()==1) { return nums[0]; }
        int current = 0;
        int seen = nums[0];
        for (int el:nums){
            if (el>current+el){ current = el; }
            else { current += el; }
            if (seen>current) { seen = seen; }
            else { seen = current; }
        }
        return seen;
    }
};
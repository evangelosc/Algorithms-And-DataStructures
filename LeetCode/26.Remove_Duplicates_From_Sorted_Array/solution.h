#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()==1) { return 1; }
        if (nums.size()==0) { return 0; }
        int s = 1, f = 1;
        //fast, slow pointers, slow pointer will point the place where you write a unique value
        while(f<nums.size()){
            if (nums[f-1]!=nums[f]){
                nums[s] = nums[f];
                s++;
            }
            f++;
        }
        return s;
    }
};
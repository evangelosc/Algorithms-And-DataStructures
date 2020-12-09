#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int first = 0, last = nums.size()-1;
        int mid;
        while (first<=last){
            mid = (int)(first+last)/2;
            if (nums[mid]<target){ first = mid + 1; }
            if (nums[mid]>=target) { last = mid - 1; }
        }
        if (nums[mid]<target){ return mid+1; }
        return mid;
    }
    int searchInsert2(vector<int>& nums2, int target){
        size_t i = 0;
        for (; i!=nums2.size(); ++i){
            if (nums2[i]==target){ return i; }
            if (nums2[i]>target) { return i; }
        }
        return i;
    }
};

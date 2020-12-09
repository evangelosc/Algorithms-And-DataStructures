#include "solution.h"

// Unit Test

int main(){
    Solution s;
    vector<int> nums1 {-2,1,-3,4,-1,2,1,-5,4};
    vector<int> nums2 {1};
    vector<int> nums3 {0};
    vector<int> nums4 {-1};
    vector<int> nums5 {-2147483647};
    if (s.maxSubArray(nums1) == 6) { cout << "Pass" << endl;}
    else { cout << "Failed 1 - t1" << endl;}
    if (s.maxSubArray(nums2) == 1) { cout << "Pass" << endl;}
    else { cout << "Failed 2 - t2" << endl;}
    if (s.maxSubArray(nums3) == 0) { cout << "Pass" << endl;}
    else { cout << "Failed 3 - t3" << endl;}
    if (s.maxSubArray(nums4) == -1) { cout << "Pass" << endl;}
    else { cout << "Failed 4 - t4" << endl;}
    if (s.maxSubArray(nums5) == -2147483647) { cout << "Pass" << endl;}
    else { cout << "Failed 5 - t5" << endl;}
    return 0;
}
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int first = m - 1;
        int second = n - 1;
        int i = m + n - 1;
        while (i>=0){
            if (second<0) { break; }
            if ((first>=0)&&(nums1[first]>nums2[second])) {
                nums1[i] = nums1[first];
                first--;
            } else {
                nums1[i] = nums2[second];
                second--;
            }
            i--;
        }
    }
};
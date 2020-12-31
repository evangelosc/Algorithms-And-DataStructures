#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res {};
        for (auto el:nums){
            res.push_back(el*el);
        }
        sort(res.begin(), res.end());
        return res;
    }
};
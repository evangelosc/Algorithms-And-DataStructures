#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> hashT;
        int idx = 0;
        for (auto el:nums){
            if (hashT.find(el)==hashT.end()){
                hashT[el] = idx;
            } else { 
                if (idx - hashT[el] <= k){
                    return true;
                }
                hashT[el] = idx;
            }
            idx++;
        }
        return false;
    }
};
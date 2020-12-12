#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        map<int, int> hMap;
        int res = 0;
        for (auto it=nums.begin(); it!=nums.end(); it++){
            if (hMap.find((*it))!=hMap.end()){
                hMap[(*it)] += 1;
            } else { hMap[(*it)] = 1;}
        }
        for (auto it=hMap.begin(); it!=hMap.end(); it++){
            if(it->second>=2) { res += (int)(it->second)*((it->second)-1)/2;}
        }
        return res;
    }
};
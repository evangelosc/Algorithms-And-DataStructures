#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        vector<int> wealth;
        for (auto client:accounts){
            int ss = 0;
            for (auto el:client){
                ss += el;
            }
            wealth.push_back(ss);
        }
        int max = wealth[0];
        for (int i=0; i!=wealth.size(); i++){
            if (wealth[i]>max){
                max = wealth[i];
            }
        }
        return max;
    }
};
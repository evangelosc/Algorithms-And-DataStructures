#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (auto it = digits.rbegin(); it!=digits.rend(); it++){
            if ((*it)<9){
                (*it) += 1;
                return digits;
            }
            *it = 0;
        }
        auto tt = digits.insert(digits.begin(), 1);
        return digits;
    }
};
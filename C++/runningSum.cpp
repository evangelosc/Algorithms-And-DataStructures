#include <vector>
#include <iostream>

class Solution {
    public:
        void runningSum(std::vector<int> &nums) {
            for(int i = 1; i < nums.size(); i++){
                nums[i] += nums[i - 1];
            }
        }
};

int main(){
    Solution sol;
    std::vector<int> theSol {1,2,3,4,5,6,7,8,9};
    sol.runningSum(theSol);
    for (int el : theSol){
        std::cout << el << " ";
    }
    std::cout << std::endl;
    return 0;
}
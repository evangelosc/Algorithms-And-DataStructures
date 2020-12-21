#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
using namespace std;

class Solution{
public:
    int getRandom(std::vector<std::vector<int>> lista){
        int randomNumber = 0;
        int totalNumber = 0;
        int currentRange = 0;
        int ans = 0;
        for (auto ranges:lista){
            totalNumber += ranges[1] - ranges[0] + 1;
        }
        srand(time(0));
        randomNumber = (rand() % totalNumber) + 1;
        for (auto ranges:lista){
            currentRange = ranges[1] - ranges[0] + 1;
            if (randomNumber<currentRange){
                ans = ranges[0] + randomNumber;
            } else {
                randomNumber -= currentRange;
            }
        }
        return ans;
    }
};
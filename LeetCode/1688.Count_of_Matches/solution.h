#include <iostream>
using namespace std;

class Solution {
public:
    int numberOfMatches(int n) {
        int sum_teams = 0;
        while (n>1){
            if (n%2==0){
                n = n/2;
                sum_teams += n;
            } else {
                n = n/2;
                sum_teams += n + 1;
            }
        }
        return sum_teams;
    }
};
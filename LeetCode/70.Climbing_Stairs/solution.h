#include <iostream>
using namespace std;


class Solution {
public:
    int climbStairs(int n) {
        if (n==0) { return 0; }
        if (n==1) { return 1; }
        if (n==2) { return 2; }
        
        int first = 1;
        int second = 2;
        int last = 0;
        int counter = 3;
        
        while(counter<=n){
            last = first+second;
            first = second;
            second = last;
            counter++;
        }
        return last;
    }
};
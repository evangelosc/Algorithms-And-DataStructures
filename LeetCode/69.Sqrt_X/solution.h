#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {  
        if (x<1) { return 0; }
        if (x<4) { return 1; }
        long first = 1;
        long last = x;
        long mid, res;
        while(first<=last){
            mid = (first+last)/2;
            if (mid <= x/mid){
                res = mid;
                first = mid + 1;
            }
            if (mid > x/mid){
                last = mid - 1;
            }
        }
        return res;
    }
};
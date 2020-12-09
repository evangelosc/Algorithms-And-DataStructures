#include <iostream>
#include <vector>
#include <string>
using namespace std;


class Solution {
public:
    bool isRobotBounded(string instructions) {
        vector<int> pos {0, 0};
        int orientation = 1;
        int circle = 4;
        for (auto el:instructions){
            if (el=='L'){
                orientation += 1;
                orientation %= circle;
            }
            if (el=='R'){
                orientation -= 1;
                orientation %= circle;
            }
            if (el=='G'){
                if (orientation == 1)
                    pos[1] += 1;
                else if (orientation == 2)
                    pos[0] -= 1;
                else if (orientation == 3)
                    pos[1] -= 1;
                else
                    pos[0] += 1;
            }
        }
        if ((orientation!=1) || (areNotZero(pos))){ return true; }
        return false;
    }
    bool areNotZero(vector<int> pos){
        if ((pos[0]==0)&&(pos[1]==0)){ return true;}
        return false;
    }
};

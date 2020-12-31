#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canWinNim(int n) {
        if (n<=3) {return true;}
        vector<bool> flag {true, true, true, true};
        int i = 4;
        while(i<=n){
            flag[0] = !flag[1] or !flag[2] or !flag[3];
            flag[3] = flag[2];
            flag[2] = flag[1];
            flag[1] = flag[0];           
            i++;
        }
        return flag[0];
    }
};
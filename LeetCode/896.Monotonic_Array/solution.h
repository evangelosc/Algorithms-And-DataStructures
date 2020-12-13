#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    struct greater
    {
      template<class T>
      bool operator()(T const &a, T const &b) const { return a>b; }
    };
    struct smaller
    {
      template<class T>
      bool operator()(T const &a, T const &b) const { return a<b; }
    };
    bool isMonotonic(vector<int>& A) {
        vector<int> init_A = A;
        sort(A.begin(), A.end(), greater());
        if (A==init_A){
            return true;
        }
        sort(A.begin(), A.end(), smaller());
        if (A==init_A){
            return true;
        }
        return false;
    }
};
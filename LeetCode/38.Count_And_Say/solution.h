#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        string curr;
        if(n==0) { return curr; }
        curr="1";
        while(n!=1){
            decode(curr);
            n--;
        }
        return curr;
    }
    void decode(string& curr){
        string res;
        int i = 0, counter = 0;
        char temp;
        while(i<curr.size()){
            temp = curr[i];
            counter = 1;
            while ((i<curr.size())&&(curr[i]==curr[i+1])){
                i++;
                counter++;
            } 
            res += to_string(counter)+temp;
            i++; 
        }
        curr = res;
    }
};
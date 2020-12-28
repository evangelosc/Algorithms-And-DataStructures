
#include <iostream>
#include <vector>
#include <tuple>
#include <limits>
using namespace std;

class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        if (x<minEl) { minEl = x; }
        stack.push_back(make_tuple(x, minEl));
    }
    
    void pop() {
        stack.pop_back();
        if (stack.size()){
            tie(x_tmp, minEl) = stack[stack.size()-1];
        } else {
            minEl = numeric_limits<int>::max();
        }
    }
    
    int top() {
        tie(x_tmp, minEl) = stack[stack.size()-1];
        return x_tmp;
    }
    
    int getMin() {
        tie(x_tmp, minEl) = stack[stack.size()-1];
        return minEl;
    }
    private:
        vector<tuple<int, int>> stack {};
        int minEl = numeric_limits<int>::max();
        int x_tmp;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
#include <iostream>
using namespace std;

int naive_GCD(int a, int b){
    // Time: O(N)
    int best = 0;
    for (int i=1; i<a+b; i++){
        if ((a%i)==0 and (b%i==0)) { 
            best = i; 
        }
    }
    return best;
}

int euclid_GCD(int a, int b){
    // Time: Log(N)
    if (b==0) { return a; }
    int alpha = a%b;
    return euclid_GCD(b, alpha); 
}

int main(){
    int a = 10;
    int b = 4;
    cout << naive_GCD(a, b) << endl;
    a = 357;
    b = 234;
    cout << euclid_GCD(a, b) << endl;
    return 0;
}
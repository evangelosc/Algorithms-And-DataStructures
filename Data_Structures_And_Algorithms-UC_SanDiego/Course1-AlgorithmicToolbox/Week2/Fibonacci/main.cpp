#include <iostream>
#include <vector>
using namespace std;

int fibonacci(int number){
    if (number == 0) { return 0; }
    if (number == 1) { return 1; }
    return fibonacci(number-1) + fibonacci(number-2);
}

vector<long long> fibonacci_fast(int number){
    vector<long long> fib;
    fib.push_back(0);
    fib.push_back(1);
    for (int i=2; i!=number; i++){
        fib.push_back((long long)fib[i-1] + fib[i-2]);
    }
    return fib;
}

int main(){
    cout << fibonacci(5) << endl;
    vector<long long> res_fibonacci_fast = fibonacci_fast(80);
    for (auto el:res_fibonacci_fast) { cout << el << endl; }
    return 0;
}
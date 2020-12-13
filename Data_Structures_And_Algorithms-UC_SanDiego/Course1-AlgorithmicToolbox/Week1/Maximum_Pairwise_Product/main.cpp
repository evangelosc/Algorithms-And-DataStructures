#include <iostream>
#include <vector>
using namespace std;

long long pairwiseProduct(vector<int> &num){
    long long result = 0;
    int index1 = -1;
    int index2 = -1;
    for (int i=0; i<=num.size(); i++){
        if (num[i]>num[index1] || index1==-1){
            index1 = i;
        }
    }
    for (int i=0; i<=num.size(); i++){
        if ((i!=index1) && (num[i]>num[index2] || index2==-1)){
            index2 = i;
        }
    }
    return (long long) num[index1]*num[index2];
}

int main(){
    int n;
    cin >> n;
    vector<int> num(n);
    for (int i=0; i<n; i++){
        cin >> num[i];
    }
    cout << pairwiseProduct(num) << endl;
    return 0;
}
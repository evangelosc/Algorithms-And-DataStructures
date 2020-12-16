#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    auto it = stops.insert(stops.begin(),0);
    stops.push_back(dist);
    int numberRefills = 0;
    int currentRefill = 0;
    int lastRefill;
    while (currentRefill<=stops.size()-2){
        lastRefill = currentRefill;
        while((currentRefill<=stops.size()-2) && ((stops[currentRefill+1]-stops[currentRefill]) <= tank )){
            currentRefill += 1;
        }
        if (currentRefill==lastRefill){
            return -1;
        }
        if (currentRefill<=stops.size()-2){
            numberRefills += 1;
        }
    }
    return numberRefills;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);
    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}

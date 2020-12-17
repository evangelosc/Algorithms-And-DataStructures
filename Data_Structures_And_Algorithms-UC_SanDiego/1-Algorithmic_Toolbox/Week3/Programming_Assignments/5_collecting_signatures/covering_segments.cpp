#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>


std::vector<int> optimal_points(std::vector<std::vector<int>> &segments) {
  std::vector<int> points;
  std::sort(segments.begin(), segments.end(),
          [](const std::vector<int>& a, const std::vector<int>& b) {
          return a[1] < b[1];
          });
  int n = segments.size();
  int current = 0;
  int last;
  while (current<n){
    last = current;
    while ((current<n-1) && (segments[current+1][0] <= segments[last][1])){
      current += 1;
      if (segments[current][1] < segments[last][1]){
        last = current;
      }
    }
    points.push_back(segments[last][1]);
    current += 1;
  }
  return points;
}

int main() {
  int n, n1, n2;
  std::cin >> n;
  std::vector<std::vector<int>> segments(n);
  for (int i=0; i!=n; i++){
    std::cin >> n1 >> n2;
    segments[i].push_back(n1);
    segments[i].push_back(n2);
  }

  std::vector<int> points = optimal_points(segments);
  std::cout << points.size() << "\n";
  for (size_t i = 0; i < points.size(); ++i) {
    std::cout << points[i] << " ";
  }
}

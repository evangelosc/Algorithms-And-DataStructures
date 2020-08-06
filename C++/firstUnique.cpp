#include <unordered_map>
#include <vector>
#include <list>
#include <iostream>

class FirstUnique{
    private:
        std::unordered_map<int, std::list<int>::iterator> _map;
        std::list<int> _keys;

    public:
        FirstUnique(std::vector<int>& nums){
            for(int n : nums){
                add(n);
            }
        }
        int showFirstUnique(){
            if(_keys.size()){
                return _keys.front();
            } else { return -1; }
        }

        void add(int value){
            if(_map.find(value) != _map.end()){
                std::list<int>::iterator it = _map[value];
                if (it != _keys.end()){
                    _keys.erase(it);
                    _map[value] = _keys.end();
                }
            } else {
                _keys.push_back(value);
                std::list<int>::iterator it = _keys.end();
                it--;
                _map[value] = it;
            }
        }
};

int main(){
    std::vector<int> x {1,1,2,2,3,4,4,5};
    FirstUnique fu(x);
    std::cout << fu.showFirstUnique() << std::endl;
    return 0;
}
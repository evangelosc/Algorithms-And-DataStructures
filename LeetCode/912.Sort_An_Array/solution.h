#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

class Solution {
public:
    // QuickSort Algorithm
    vector<int> sortArray_qs(vector<int> &nums){
        int left = 0;
        int right = nums.size()-1;
        Quicksort(nums, left, right);
        return nums;
    }
    void Quicksort(vector<int> &nums, int left, int right){
        if (left>=right){return;}
        int m = partition(nums, left, right);
        Quicksort(nums, left, m-1);
        Quicksort(nums, m+1, right);
    }
    int partition(vector<int> &nums, int left, int right){
        int pivot = nums[left];
        int j = left;
        for (int i=left+1; i!=right+1; i++){
            if (nums[i]<=pivot){
                j++;
                std::tie(nums[i], nums[j]) = swap(nums[i], nums[j]);
            }
        }
        std::tie(nums[j], nums[left]) = swap(nums[j], nums[left]);
        return j;
    }
    std::tuple<int, int> swap(int el1, int el2){
        int tmp = el1;
        el1 = el2;
        el2 = tmp;
        return std::make_tuple(el1, el2);
    }
        
    // MergeSort Algorithm
    vector<int> sortArray_ms(vector<int> &nums){
        if (nums.size()==1) { return nums; }
        int m = ((nums.size()-1)/2);        
        vector<int> B, C, D, B_t, C_t;
        for (int i=0; i!=m+1; i++){
            B_t.push_back(nums[i]);
        }
        for (int i=m+1; i!=nums.size(); i++){
            C_t.push_back(nums[i]);
        }
        B = sortArray_ms(B_t);
        C = sortArray_ms(C_t);
        D = merge(B, C);
        return D;
    }
    int find_idx(vector<int> vec, int n){
        int res = -1;
        for(int i=0; i!=vec.size(); i++){
            if(vec[i]==n){res=i;}
        }
        return res;
    }
    vector<int> merge(vector<int> B, vector<int> C){
        vector<int> res;
        int idx;
        while (B.size()!=0 && C.size()!=0){
            int b = B[0];
            int c = C[0];
            if (b<=c){
                res.push_back(b);
                idx = find_idx(B, b);
                B.erase(B.begin()+idx);
            } else {
                res.push_back(c);
                idx = find_idx(C, c);
                C.erase(C.begin()+idx);
            }
        }
        if (B.size()!=0){
            for (auto el:B){
                res.push_back(el);
            }
        }
        if (C.size()!=0){
            for (auto el:C){
                res.push_back(el);
            }
        }
        return res;
    }
    // // SelectionSort Algorithm
    vector<int> sortArray_ss(vector<int>& nums) {
        for(int i=0; i!=nums.size(); i++){
            int minIdx = i;
            for (int j=i+1; j!=nums.size(); j++){
                if (nums[j]<nums[minIdx]){
                    minIdx = j;
                }
            }
            std::tie(nums[i], nums[minIdx]) = swap(nums[i], nums[minIdx]);
        }
        return nums;
    }
    std::tuple<int, int> swap(int el1, int el2){
        int tmp = el1;
        el1 = el2;
        el2 = tmp;
        return std::make_tuple(el1, el2);
    }
};
#!/usr/bin/python

class Quick(object):
    # QuickSort Algorithm
    # Average Time Complexity: O(N)
    # Space: O(N)
    def sortArray(self, nums):
        self.Quicksort(nums, 0, len(nums)-1)
        return nums
    
    def Quicksort(self, nums, left, right):
        if (left>=right):
            return
        m = self.partition(nums, left, right)
        self.Quicksort(nums, left, m-1)
        self.Quicksort(nums, m+1, right)
        
    def partition(self, nums, left, right):
        pivot = nums[left]
        j = left
        for i in range(left+1, right+1):
            if nums[i]<=pivot:
                j += 1
                nums[i], nums[j] = self.swap(nums[i], nums[j])
        nums[left], nums[j] = self.swap(nums[left], nums[j])
        return j
    
    def swap(self, el1, el2):
        tmp = el1
        el1 = el2
        el2 = tmp
        return el1, el2

class Merge(object):
    # MergeSort Algorithm
    # Time: O(NlogN)
    # Space: O(N)
    def sortArray(self, nums):
        if len(nums)==1:
            return nums
        m = len(nums)//2
        B = self.sortArray(nums[:m])
        C = self.sortArray(nums[m:])
        D = self.merge(B, C)
        return D
    def merge(self, B, C):
        D_prime = list()
        while (len(B)!=0 and len(C)!=0):
            b = B[0]
            c = C[0]
            if (b<=c):
                D_prime.append(b)
                B.remove(b)
            else:
                D_prime.append(c)
                C.remove(c)
        if len(B):
            for el in B:
                D_prime.append(el)
        if len(C):
            for el in C:
                D_prime.append(el)
        return D_prime

class Selection(object):
    # SelectionSort Algorithm
    # Time: O(N^2)
    # Space: O(1)
    def sortArray(self, nums):
        for i in range(len(nums)):
            minIdx = i
            for j in range(i+1, len(nums)):
                if nums[j]<nums[minIdx]:
                    minIdx = j
            nums[i], nums[minIdx] = self.swap(nums[i], nums[minIdx])
        return nums
        
    def swap(self, el1, el2):
        tmp = el1
        el1 = el2
        el2 = tmp
        return el1, el2
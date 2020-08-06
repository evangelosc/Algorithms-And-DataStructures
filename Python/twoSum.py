# Problem: Given an array of integers, 
# return indices of the two numbers such that they add up to a specific target. 
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# def binarySum(nums, target):
#     if len(nums) < 2:
#         return False
#     nums = sorted(nums) #O(NlogN)
#     low = 0
#     high = len(nums) - 1
#     while low <= high:
#         mid = low + (high-low)//2
#         if nums[mid] > target:
#             high = mid - 1
#         elif nums[mid] < target:
#             low = mid + 1



def twoSum(nums, target):
    if len(nums) < 2:
        return False
    hashT = dict()
    count = 0
    for el in nums:
        if el in hashT:
            return hashT[el], count
        else:
            hashT[target-el] = count
        count += 1
    return False


print(twoSum([1,3,11,2,7],9))
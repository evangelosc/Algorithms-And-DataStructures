def dublicate(nums):
    for i in range(len(nums)):
        if nums[abs(nums[i])-1] < 0:
            return abs(nums[i])
        else:
            print(nums)
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
    return -1

print(dublicate([1,3,4,2,2]))
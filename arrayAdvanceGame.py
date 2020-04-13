def AAGame(nums):
    el = 1
    for x in nums[:-1]:
        el = max(x, el-1)
        if el == 0:
            return False 
    return True

print(AAGame([0,1]))
print(AAGame([3,3,1,0,2,0,1]))
print(AAGame([3,2,0,0,2,0,1]))
# In this video, we will be given a sorted array and a target number. 
# Our goal is to find a number in the array that is closest to the target number. 
# We will be making use of binary search to solve this problem.

# The array may contain duplicate values and negative numbers.

# Example 1:
#     Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
#     Target number = 11
#     Output : 9
#     9 is closest to 11 in given array

# Example 2:
#     Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
#     Target number = 4
#     Output : 5
def findClosestValue(lista, target):
    low = 0 
    high = len(lista)-1
    minDiff = float('Inf')
    closetNum = None
    
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        return lista[0]
    while low<=high:
        mid = low + (high-low)//2
        # Ensure we do not read beyond the bounds of the list and take the
        # left and right values
        if mid + 1 < len(lista):
            minRight = abs(lista[mid+1]-target)
        if mid > 0:
            minLeft = abs(lista[mid-1]-target)

        # Check if the ABS between left and right elements are smaller than any seen prior
        if minLeft < minDiff:
            minDiff = minLeft
            closetNum = lista[mid-1]
        if minRight < minDiff:
            minDiff = minRight
            closetNum = lista[mid+1]

        # Move the mid point accordingly binary search
        if lista[mid] < target:
            low = mid + 1
        elif lista[mid] > target:
            high = mid - 1
        else:
            return lista[mid]   
    return closetNum    


print(findClosestValue([1,2,4,5,6,6,8,9], 11))
    
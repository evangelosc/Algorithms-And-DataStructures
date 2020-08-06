# In this video, we will be writing a function that computes the integer square root 
# of a given number as input without using any built-in square root function.

# Specifically, write a function that takes a non-negative integer and returns 
# the largest integer whose square is less than or equal to
# the integer given:

# Example:

# Assume input is integer 300.
    
# Then the expected output of the function should be 17 since 17 squared 
# is 289 which is strictly less than 300. Note that 18 squared is 324 
# which is strictly greater than 300, so the number 17 is the correct response.
import math
def integerSqrt(num):
    low = 0
    high = num
    while low <= high:
        mid = low + (high-low)//2
        midSquared = mid**2
        if midSquared <= num:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

print(integerSqrt(300))



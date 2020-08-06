# An array is "cyclically sorted" if it is possible to cyclically shift
# its entries so that it becomes sorted.
# The following list is an example of a cyclically sorted array:

#     A = [4, 5, 6, 7, 1, 2, 3]

# Write a function that determines the index of the smallest element
# of the cyclically sorted array.

def cyclicSwift(lista):
    low = 0
    high = len(lista) - 1
    while low < high:
        mid = (low+high)//2
        if lista[mid] > lista[high]:
            low = mid + 1
        elif lista[mid] <= lista[high]:
            high = mid
    return low

print(cyclicSwift([4,5,6,7,1,2,3]))
         
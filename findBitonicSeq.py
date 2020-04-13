# In this video, we will be given an array that is bitonically sorted, 
# an array that starts off with increasing terms and then concludes with 
# decreasing terms. In any such sequence, there is a "peak" element, that is, 
# the element in the sequence that is the largest element. We will be writing 
# a problem to help us in finding the peak element of a bitonic sequence. 

def findMaxN(lista):
    # Time: O(logN)
    # Space: O(1)
    if len(lista) < 3:
        return None
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = low + (high-low)//2
        if lista[mid] > lista[mid-1] and lista[mid] < lista[mid+1]:
            low = mid + 1
        elif lista[mid] < lista[mid-1] and lista[mid] > lista[mid+1]:
            high = mid - 1
        elif lista[mid] > lista[mid-1] and lista[mid] > lista[mid+1]:
            return lista[mid]
        else:
            print("idk if there are other cases")
    return False

print(findMaxN([1,2,3,4,1])) 
print(findMaxN([1,6,5,4,3,2,1]))
print(findMaxN([1,2,3,4,5,4,3,2,1]))
print(findMaxN([0,1,0]))
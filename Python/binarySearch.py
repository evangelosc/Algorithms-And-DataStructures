class binarySearch(object):
    def __init__(self, key, lista):
        self.key = key
        self.lista = lista
        self.low = 0
        self.high = len(self.lista)-1

    def theBinarySearch(self):
        while(self.low<=self.high):
            mid = self.low + (self.high-self.low)//2
            if self.key < self.lista[mid]:
                self.high = mid-1
            elif self.key > self.lista[mid]:
                self.low = mid+1
            else:
                return mid
        return False
    
    def theBinarySearchRec(self, low, high, count):
        if count==1:
            low = self.low
            high = self.high
        if low > high:
            return False
        else:
            count += 1
            mid = low + (high-low)//2
            if self.key == self.lista[mid]:
                return mid
            elif self.key < self.lista[mid]:
                return self.theBinarySearchRec(low, mid-1, count)
            else:
                return self.theBinarySearchRec(mid+1, high, count)


data = [2,4,5,7,8,9,12,17,19]
search = binarySearch(7, data)
print(search.theBinarySearch())
print(search.theBinarySearchRec(0,0,1))
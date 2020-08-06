class MovingTotal:
    def __init__(self):
        self.items = list()
        self.hashT = dict()
        self.index = 0

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        if len(self.items) == 0:
            self.items.append(numbers)
            self.hashT[self.index] = sum(self.items) 
        else:
            self.items.pop(0)
            self.items.extend(numbers)
            self.hashT[self.index] = sum(self.items)
            self.index += 1

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        for _, values in self.hashT:
            if values == total:
                return True
        return False
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    movingtotal.append([4])
    print(movingtotal.contains(9))
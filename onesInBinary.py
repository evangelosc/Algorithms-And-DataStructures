# Problem: Find the number of 1s in the binary representation of a number. For example:

# num_ones(2) = 1 -- since "10" is the binary representation of the number "2". 

# num_ones(5) = 2 -- since "101" is the binary representation of the number "5"

# num_ones(11) = 3 -- since "1011" is the binary representation of the number "11"

def intToBinary(num):
    sumT = 0
    while num:
        sumT += num & 1
        num >>= 1 # num//2
    return sumT
print(intToBinary(5))
# In this video, we will be considering the so-called "Look-and-Say" sequence. 
# The first few terms of the sequence are:

# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... 

# To generate a member of the sequence from the previous member, 
# read off the digits of the previous member, counting the number of digits 
# in groups of the same digit. For example:

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 1211 is read off as "one 1, one 2, then two 1s" or 111221.
# 111221 is read off as "three 1s, two 2s, then one 1" or 312211.

# More information on the properties of this sequence can be found on the 
# Wikipedia page here:
# https://en.wikipedia.org/wiki/Look-an...

# We will define the "look-and-say" sequence and also determine a way to 
# generate the nth term in the sequence. We will also code up an implementation 
# in Python that calculates the nth term in the "look-and-say" sequence. 

def nextNumber(theStr):
    i = 0
    theRes = list()
    while i < len(theStr):
        count = 1
        while i + 1 < len(theStr) and theStr[i] == theStr[i+1]:
            i += 1
            count += 1
        theRes.append(str(count) + theStr[i])
        i += 1
    return ''.join(theRes)

s = "1"
N = 5
for i in range(N-1):
    s = nextNumber(s)
    print(s)
print(nextNumber("1211"))
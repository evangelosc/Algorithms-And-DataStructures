# Problem:
# String Compression: Implement a method to perform basic string 
# compression using the counts of repeated characters. 
# For example, the string "aabcccccaaa" would become a2b1c5a3. 
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a-z).

s1 = 'aabcccccaaa'

def strCompression(theStr):
    count = 1
    comp = ''
    for i in range(len(theStr)-1):
        if theStr[i] == theStr[i-1]:
            count += 1
        else:
            comp += theStr[i] + str(count)
            count = 1
    comp += theStr[i] + str(count)
    if len(comp) >= len(theStr):
        return theStr        
    else:
        return comp
        
print(strCompression(s1))
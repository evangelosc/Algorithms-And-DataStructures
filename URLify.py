# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the 
# end to hold the additional characters and that you are given 
# the "true" length of the string.

def urlFun(theStr):
    url = ''
    for el in theStr:
        if el == ' ':
            url += '%20'
        else:
            url += el
    return url

print(urlFun('Mr. John Smith'))

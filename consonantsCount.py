# Given a string, calculate the number of consonants present using recursion.
# Vowels: a,e,i,o,u

def consonantsCount(newStr):
    vowels = "aeiou"
    count = 0
    for x in newStr:
        if x not in vowels and x.isalpha():
            count += 1
            # print(str(x)+" is a vowel.")
    return count

def consonantsCountRec(newStr):
    vowels = "aeiou"
    if newStr == "":
        return 0
    if newStr[0] not in vowels and newStr[0].isalpha():
        return 1 + consonantsCountRec(newStr[1:])
    else:
        return consonantsCountRec(newStr[1:])


print(consonantsCount("malak1"))
print(consonantsCountRec("malaka"))
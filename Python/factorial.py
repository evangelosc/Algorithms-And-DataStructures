# Factorial recursively and iteratively

def factRec(num):
    if not str(num).isnumeric() and num < 0:
        return False
    if num < 2:
        return 1
    return num*factRec(num-1)

print(factRec(5))

def fact(num):
    product = 1
    for i in range(num+1):
        if i == 0:
            continue
        else:
            product *= i
            print(product, i)
    return product

print(fact(5))
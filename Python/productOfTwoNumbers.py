    # Given two numbers, find their product using recursion.

def productRec(x, y):
    # This cuts down the total number of rec calls
    if x < y:
        return productRec(y,x)
    if x < 0 or y < 0:
        return ("Not applicable for negative numbers")
    if y == 0:
        return 0
    return x + productRec(x, y-1)

print(productRec(500,3000))
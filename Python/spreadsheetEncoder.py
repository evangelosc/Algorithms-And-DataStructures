def spreadsheetEncoder(colStr):
    num = 0
    count = len(colStr) - 1
    for el in colStr:
        num += ((26**count) * (ord(el)-ord('A')+1) )
        count -= 1
    return num

print(spreadsheetEncoder('AAA'))
print(spreadsheetEncoder('Z'))
print(spreadsheetEncoder('AA'))
print(spreadsheetEncoder('ABCDF'))


def num2SpreadSheet(n):
    string = ""
    while n > 0:
        n,remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

print(num2SpreadSheet(26))
print(num2SpreadSheet(27))
print(num2SpreadSheet(28))
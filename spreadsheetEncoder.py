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
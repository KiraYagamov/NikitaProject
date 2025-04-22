arr = [1, 1, 2]
newArr = []
for el in arr:
    if el not in newArr:
        newArr.append(el)
print(newArr)

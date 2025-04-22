arr = [1, 2, 3, 4]

for i in range(len(arr)//2):
    first = arr[i]
    arr[i] = arr[-1-i]
    arr[-1-i] = first
print(arr)

n = 3
k = 5

for i in range(n):
    for j in range(1, k + 1):
        print(j if i % 2 == 0 else k-j+1)

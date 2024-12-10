line = "Hello world"
simbols = {}

for i in line:
    simbols[i] = line.count(i)

for c in range(3):
    maxSim = 0
    maxCount = 0
    for i in simbols.keys():
        if maxCount < simbols[i]:
            maxCount = simbols[i]
            maxSim = i
    print(maxSim)
    simbols.pop(maxSim)

line = input()
numbers = "1234567890"
minNumber = 10

for i in range(len(line)):
    if line[i] in numbers:
        if int(line[i]) < minNumber:
            minNumber = int(line[i])

if minNumber == 10:
    print("Нет цифр!")
else:
    print(minNumber)

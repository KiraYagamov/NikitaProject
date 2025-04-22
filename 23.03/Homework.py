line = input()
numbers = "1234567890"
inlineCount = 0
maxInline = 0
for i in range(len(line)):
    if line[i] in numbers:
        inlineCount += 1
    else:
        maxInline = max(maxInline, inlineCount)
        inlineCount = 0
print(maxInline)

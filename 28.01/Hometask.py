sim = "*"
size = 7
left = 0
right = size-1

for i in range(size):
    if i == 0 or i == size-1:
        print(sim*size)
    else:
        line = ""
        for j in range(size):
            if j == left or j == right:
                line += sim
            else:
                line += " "

        print(line)
    left += 1
    right -= 1

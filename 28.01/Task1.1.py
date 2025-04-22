width = 33
sim = "*"
left = 0
right = width-1


# Вывод верхних холмов
left_left = 0
right_left = left_right = width // 2
right_right = width-1
lines = []

while True:
    line = ""
    for i in range(width):
        if left_left <= i <= right_left or left_right <= i <= right_right:
            line += sim
        else:
            line += " "
    lines.append(line)
    if right_left - left_left <= width // 4:
        break
    left_left += 1
    right_left -= 1
    left_right += 1
    right_right -= 1

lines.reverse()
for line in lines:
    print(line)

# Вывод нижнего треугольника
while True:
    line = ""
    for i in range(width):
        if left <= i <= right:
            line += sim
        else:
            line += " "
    print(line)
    if left >= right:
        break
    left += 1
    right -= 1

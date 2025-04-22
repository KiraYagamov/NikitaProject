width = 9
sim = "*"
left = 0
right = width-1

# Вывод двух верхних холмов
print(" " + (width // 4) * sim + (width - (width // 4)*2 - 2) * " " + (width // 4) * sim)
print((width // 2) * sim + (width - (width // 2)*2) * " " + (width // 2) * sim)

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

# Ромб

scale = 9

left = right = scale // 2
if scale % 2 == 0:
    right += 1

while left != 0:
    for i in range(scale+1):
        if left <= i <= right:
            print("#", end="")
        else:
            print(" ", end="")
    print()
    left -= 1
    right += 1

left += 1
right -= 1

while left != scale // 2:
    left += 1
    right -= 1
    for i in range(scale+1):
        if left <= i <= right:
            print("#", end="")
        else:
            print(" ", end="")
    print()

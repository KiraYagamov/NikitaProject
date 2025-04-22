radius = 30
coeff = 2

for y in range(radius, -radius -1, -1):
    for x in range(int(-radius*coeff), int(radius*coeff) + 1):
        if y < 0 and (x/coeff)*(x/coeff) + y*y <= radius * radius:
            print("#", end="")
        elif (x/coeff)*(x/coeff) + y*y < radius * radius:
            print("#", end="")
        else:
            print(" ", end="")
    print()
input()
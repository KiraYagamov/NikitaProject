from random import randint

size = 10
ship_size = 3
field = [0 for i in range(size)]

ship_place = randint(0, size - ship_size)

for i in range(ship_place, ship_place + ship_size):
    field[i] = 1

print(field)

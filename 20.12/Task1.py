sum_count = int(input("Введите количество чисел в сумме: "))
summa = 0
for i in range(sum_count):
    num = int(input(f"Введите {i+1} число: "))
    summa += num
if summa % 2 == 0:
    print("Четная сумма")
else:
    print("Нечетная сумма")

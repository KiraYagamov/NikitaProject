# Переменные
# x = 4
# y = 2

# print(x + y)

# Операция остатка от деления - %
# x % 2 == 0 - число четное
# x % 2 != 0 - число нечетное

# Условия

# x = input("Введите число: ")
# x = int(x)

# print("X =", x)

# if x > 5:
#     print("X больше 5")
# elif x < 5:
#     print("X меньше 5")
# else:
#     print("X равен 5")

# print("Блок завершен!")

# if x == 15:
#     print("X равен 15")

# print("Программа завершена!")


# Решение задачи

# x = int(input("Введите число: "))
#
# if x % 2 == 0:
#     print("Число четное!")
# else:
#     print("Число нечетное!")
#
# print("Конец программы")

# Калькулятор

# num1 = float(input("Введите первое число: "))
# operation = input("Введите операцию: ")
# num2 = float(input("Введите второе число: "))
#
# if operation == "+":
#     print("Ответ: " + str(num1 + num2))
# elif operation == "-":
#     print("Ответ: " + str(num1 - num2))
# elif operation == "*":
#     print("Ответ: " + str(num1 * num2))
# elif operation == "/":
#     if num2 != 0:
#         print("Ответ: " + str(num1 / num2))
#     else:
#         print("Деление на 0 запрещено!")
# else:
#     print("Я не знаю такой операции!")

# Циклы

# summa = 0
# for i in range(1, 10 + 1):
#     summa += i
# print(summa)


# result = ""
# for i in range(100 + 1):
#     result += str(i) + " "
# print(result)


# i = 0
# while i < 10:
#     print("Hello world", i)
#     i += 1


# for x in range(1, 3 + 1):
#     for y in range(1, 3 + 1):
#         print(x*y, end=" ")
#     print()


# x = ["в", "б", "ф", "д"]
#
# x.sort()
# print(x)


# chet = []
# tr = []
# five = []
#
# for i in range(1, 50+1):
#     if i % 2 == 0:
#         chet.append(i)
#     if i % 3 == 0:
#         tr.append(i)
#     if i % 5 == 0:
#         five.append(i)
#
# print(chet)
# print(tr)
# print(five)


# a = [i for i in range(10) if i % 2 == 0]
# print(a)


# a = []
# for i in range(1, 10+1):
#     a.append(i*i)
# print(a)

# a = [i*i for i in range(1, 10+1)]
# print(a)


# line = "Привет мир Привет мир Привет мир"
# a = 5
# b = 8
# line = f"{a} + {b}"
# print(line)


# task = input("Введите пример: ")
# values = task.split()
# if len(values) > 1:
#     if values[1] == "+":
#         print(f"Ответ: {float(values[0]) + float(values[2])}")
#     elif values[1] == "-":
#         print(f"Ответ: {float(values[0]) - float(values[2])}")
#     elif values[1] == "*":
#         print(f"Ответ: {float(values[0]) * float(values[2])}")
#     elif values[1] == "/":
#         print(f"Ответ: {float(values[0]) / float(values[2])}")
#     else:
#         print("Такой операции нет!")
# else:
#     if values[0][-1] == "!":
#         result = 1
#         for i in range(2, int(values[0][:-1]) + 1):
#             result *= i
#         print(f"Ответ: {result}")
#     else:
#         print("Ошибка!")


# humans = {
#     "Ivan": 20,
#     "Petya": 15,
#     "Vasya": 10,
#     "Vitya": 20
# }
#
# for name in humans.keys():
#     print(f"Возраст {name}: {humans[name]} лет")


# def print_matrix(matrix):
#     for arr in matrix:
#         strArr = [str(i) for i in arr]
#         line = " | ".join(strArr)
#         print(line)
#
#
# def shoot(matrix, x, y, step):
#     if step % 2 == 0:
#         matrix[x][y] = "X"
#     else:
#         matrix[x][y] = "O"
#
# matrix = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " "]
# ]
# step = 0
# while True:
#     print_matrix(matrix)
#     posX, posY = map(int, input("Введите позицию: ").split())
#     if posX == -1 or posY == -1:
#         break
#     shoot(matrix, posX, posY, step)
#     step += 1
#
# print("Игра завершена!")

# def program():
#     try:
#         num1 = int(input("Первое число: "))
#         num2 = int(input("Второе число: "))
#         print(num1 / num2)
#     except ValueError:
#         print("Ошибка! Введите число!")
#         program()
#     except ZeroDivisionError:
#         print("Ошибка! Деление на 0 запрещено!")
#         program()
#
# program()
# print("Конец программы")


# def fact(num):
#     result = 1
#     for i in range(2, num+1):
#         result *= i
#     return result
#
# print(fact(1000))


# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * fact(num-1)
#
# print(fact(998))

# def binary_tree(steps=3, was=""):
#     if steps == 0:
#         return
#     for i in range(2):
#         val = was + str(i)
#         print(val)
#         binary_tree(steps - 1, val)
#
# binary_tree(50)


def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Деление на 0 запрещено!"
    return num1 / num2

num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))

print(divide(num1, num2))

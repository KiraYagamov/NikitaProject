months = ["Январь", "Февраль", "Март", "Апрель",
          "Май", "Июнь", "Июль", "Август",
          "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
try:
    month = int(input())
    print(months[month-1] if 1 <= month <= 12 else "Такого месяца нет!")
except ValueError:
    print("Некорректное число!")

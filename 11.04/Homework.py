def get_max_digit(line):
    numbers = "0123456789" # Сторка из цифр для определения цифры
    max_digit = -1 # Начальное значение максимальной цифры
    for el in line: # Перебираем все символы строки
        if el in numbers: # Если символ является цифрой...
            if max_digit < int(el): # Если эта цифра больше, чем текущая максимальная...
                max_digit = int(el) # Меняем значение максимальной на текущую
    return max_digit # Возвращаем максимальную цифру

print(get_max_digit(input()))

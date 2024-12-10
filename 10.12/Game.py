from random import randint
from Bot import Bot

# Константы
left = 1
right = 10
bots_count = 5

# Перменные игровой логики
question = randint(left, right)
is_game_ended = False

# Переменные ботов
bots = []
names = ["Вася", "Петя", "Витя", "Робот", "Бoт1", "Кирилл", "Шарик", "Бобик", "Рома", "Принтер"]

# Создание ботов
for i in range(bots_count):
    name = names[randint(0, len(names)-1)]
    bot = Bot(i+1, name, left, right)
    bots.append(bot)

# Логика игры
while not is_game_ended:
    ask = int(input("Ваш вариант: "))
    if ask == question:
        print("Вы угадали!")
        is_game_ended = True
        break
    else:
        print("Вы не угадали!")
    for bot in bots:
        ask = bot.ask()
        if ask == question:
            print("И он угадал!")
            is_game_ended = True
            break
        else:
            print("И он не угадал :(")
print("Игра окончена!")

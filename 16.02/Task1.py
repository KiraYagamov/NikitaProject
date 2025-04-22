# Задача:
# Написать программу с формой регистрации и последующем входом в аккаунт

# Пример:
# Пожалуйста, зарегистрируйтесь!
# Логин: testlogin
# Пароль: password

# Войдите в аккаунт:
# Логин: test
# Пароль: test
# Такого аккаунта не существует, попробуйте ещё раз!

# Логин: testlogin
# Пароль: pass
# Неверный пароль! Попробуйте еще раз!

# Логин: testlogin
# Пароль: password
# Успешный вход!

print("Пожалуйста, зарегистрируйтесь!")
login = input("Логин: ")
password = input("Пароль: ")

print()
print("Войдите в аккаунт:")
while True:
    trylogin = input("Логин: ")
    trypassword = input("Пароль: ")
    if login != trylogin:
        print("Такого аккаунта не существует, попробуйте ещё раз!")
        print()
        continue
    elif trypassword != password:
        print("Неверный пароль! Попробуйте еще раз!")
        print()
        continue
    else:
        print("Успешный вход!")
        break

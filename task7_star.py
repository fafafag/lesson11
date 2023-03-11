data = {}

def login(log, pas):
    if data.get(log) == None:
        data[log] = pas
        print("Регистрация прошла успешно")
        return
    if data.get(log) == pas:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")


print("Введите логин")
log = input()

print("Введите пароль")
pas = input()

login(log, pas)
print(data)
spisok = []
print("Введите имя")


def hello(name):
    if name in spisok:
        return "Привет," + name + "!"
    else:
        spisok.append(name)
        return "Привет," + name + "! Рад знакомству!"


name = input()
print(hello(name))
print(spisok)

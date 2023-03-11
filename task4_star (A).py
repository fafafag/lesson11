def count():
    odd = 0  # четные
    mean = 0  # нечетные
    n = int(input())
    i = 1
    while i <= n:  # <- базовый случай
        if i % 2 == 0:
            odd += 1
        else:
            mean += 1
        i += 1  # <- рекурсивный случай
    return f'четные {odd}, нечетные {mean}'


print(count())

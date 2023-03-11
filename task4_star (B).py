def count(odd = 0, mean = 0, n = int(input()), i = 1):
    # while i <= n: # <- базовый случай
    if i > n:
        return f'четные {odd}, нечетные {mean}'
    if i % 2 == 0:
        odd += 1
    else:
        mean += 1
    return count(odd, mean, n, i+1) # <- рекурсивный случай
print(count())
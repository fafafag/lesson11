def factorial(n = int(input()), rez = 1):
    # while n >= 1:
    if n < 1:
        return rez
    rez *= n
    return factorial(n - 1, rez)


print(factorial())
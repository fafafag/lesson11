def factorial():
    n = int(input())
    rez = 1
    while n >= 1:
        rez *= n
        n -= 1
    return rez
print(factorial())
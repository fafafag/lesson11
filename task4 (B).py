i = 0
def count():
    global i
    if i <= 10:
        print(i, "\n")
        i += 1
        count()
count()
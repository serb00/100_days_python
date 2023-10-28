def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(5, 4, 2, 1))

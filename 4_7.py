def fact(n):
    f = (el for el in range(1, n + 1))
    fact = 1
    for i in f:
        fact *= i
        yield i, fact


for num,j in fact(int(input('Введите N: '))):
    print(f'{num}!={j}')

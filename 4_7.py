def fact(n):
    f = (el for el in range(1, n + 1))
    fact = 1
    for i in f:
        fact *= i
        yield fact


for j in fact(int(input('Введите N: '))):
    print(j)

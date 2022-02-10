from functools import reduce


def sum_f(x, y):
    return x * y


my_list = [x for x in range(100, 1001, 2)]
print(reduce(sum_f, my_list))

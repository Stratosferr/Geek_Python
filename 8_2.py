class MyError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg


# Вариант 1
print("Вариант 1")
inp_delimoe = float(input('Введите делимое: '))

while True:
    inp_delitel = float(input('Введите делитель:'))
    try:
        if inp_delitel == 0:
            raise MyError("Делитель не может быть равен нулю!\nПовторите ввод.")
        else:
            break
    except MyError as err:
        print(err.error_msg)

print(inp_delimoe / inp_delitel)

# Вариант 2
print("Вариант 2")
a = float(input('Введите делимое: '))

while True:
    b = float(input('Введите делитель:'))
    try:
        c = a / b
    except ZeroDivisionError as err:
        try:
            raise MyError("Делить на ноль нельзя, повторите ввод!")
        except MyError as m:
            print(m)
    else:
        break

print(c)

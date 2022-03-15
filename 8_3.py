class OnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
print(
    "Вводите значения для списка, только числа.\n"
    "Числа могут быть любыми вещественными\nЧтобы закончить ввод введите 'q'")

while True:
    digit = input(f'Введите{" следующее " if len(my_list) != 0 else " "}число для добавления в список:')
    try:
        digit = digit.replace(',', '.')
        if digit in "qQйЙ":
            break
        if (digit.replace('.', '').isdigit()) and (digit.count('.') in [0, 1]):
            if digit.count('.') == 0:
                my_list.append(int(digit))
            else:
                my_list.append(float(digit))
        else:
            raise OnError("Вы ввели не число, повторите ввод")

    except OnError as err:
        print(err)

print(f'Ваш список:\n{my_list}')

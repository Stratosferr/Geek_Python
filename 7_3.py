class Sell():
    def __init__(self, nucleos):
        self.nucleos = int(nucleos)

    def __add__(self, other):
        return f"После сложения в общей клетке {self.nucleos + other.nucleos} ячеек"

    def __sub__(self, other):
        return f"В результате вычитания в общей клетке осталось {abs(self.nucleos - other.nucleos)} ячеек" if self.nucleos != other.nucleos else "В клетках одинаковое количество ячеек"

    def __mul__(self, other):
        return f"В общей клетке при умножении {self.nucleos * other.nucleos} ячеек"

    def __truediv__(self, other):
        if other.nucleos == 0 or self.nucleos == 0:
            return "Количество ячеек в одной из клеток равно 0. Деленое на ноль невозможно"
        return f"В общей клетке при делении остается {max(self.nucleos, other.nucleos) // min(self.nucleos, other.nucleos)} ячеек" if min(
            self.nucleos, other.nucleos) != 0 else f"Деление на ноль невозможно. Одна из клеток не содержит ячеек"

    def make_order(self, nums_in_str):
        if nums_in_str == 0:
            print('количество клеток в строке равно 0. Деление на ноль невозможно')
        else:
            for i in range(self.nucleos // nums_in_str):
                print('*' * nums_in_str)
            print("*" * (self.nucleos % nums_in_str))


sell_1 = Sell(19)
sell_2 = Sell(57)
print(sell_2 + sell_1)
print(sell_2 - sell_1)
print(sell_2 * sell_1)
print(sell_2 / sell_1)
sell_1.make_order(int(input('Введите количество ячеек в строке: ')))

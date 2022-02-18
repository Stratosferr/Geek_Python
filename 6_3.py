class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


a = Position(input('Имя: '), input('Фамилия: '), input('Должность: '),
             {"wage": float(input('оклад: ')), "bonus": float(input('Премия: '))})
print(a.get_full_name(), a.get_total_income())

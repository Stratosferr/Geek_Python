class Date:
    def __init__(self, date_str):
        self.__date_str = date_str
        self.split_date(self.__date_str)

    @classmethod
    def split_date(cls, date_str):
        cls.__day, cls.__month, cls.__year = cls.check_date(date_str)

    @staticmethod
    def check_date(var):
        v_list = var.split('.')

        if len(v_list) < 3:
            exit("Не верный формат даты, должен быть 'dd.mm.yyyy'")

        try:
            v_list = list(map(int, v_list))
        except ValueError:
            exit("Ошибка!\nКаждый элемент даты должен быть целым числом")

        if v_list[0] not in range(1, 32):
            exit("День должен быть целым числом в промежутке от 1..31")
        if v_list[1] not in range(1, 13):
            exit("Месяц должен быть целым числом в промежутке от 1..12")
        if v_list[2] < 0:
            exit("Год должен быть в целым числом")

        return v_list

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year


d = Date('28.05.2122')
print(d)
print(f"Day={d.day}, Month={d.month}, Year={d.year}")

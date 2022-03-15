class Storage:
    def __init__(self, name, max_count):
        """ Конструктор, инициализирует атрибуты:\n
            :param name: string Название склада
            :param max_count: int Максимальная вместительность
        """
        self.__name = name
        self.__max_count = max_count
        self.__current_count = 0
        self.store = {}

    @property
    def get_store_capacity(self):
        """ Возвращает максимальную заполняемость склада\n
            :return int
        """
        return self.__max_count

    @property
    def get_current_capacity(self):
        """ Возвращает текущую заполненность склада\n
            :return int
        """
        return self.__current_count

    @property
    def get_free_capacity(self):
        """ Возвращает кол-во свободного места на складе\n
            :return int
        """
        return self.__max_count - self.__current_count

    @property
    def is_full(self):
        """ Проверяет полный ли склад уже\n
            :return True - если клад полный\n
            :return False - если склад не полный
        """
        return self.__max_count == self.__current_count

    @property
    def name(self):
        """ Возвращает название склада\n
            :return string
        """
        return self.__name

    def put_in_storage(self, oe):
        """ Помещает объект подкласса OfficeEquipment на склад\n
            Если такой объект уже есть на складе,\n
            то выводит соответсвующее предупреждение,\n
            и возвращает False\n
            Если объекта нет на складе,\n
            то добавляет объект на склад, в соответствующую секцию,\n
            В зависимости от типа объекта и возвращает True
        """

        if oe is not None:
            if not self.is_full:
                if oe.type in self.store:
                    if oe not in self.store[oe.type]:
                        self.store[oe.type].append(oe)
                    else:
                        print(f"Товар {oe.name} уже находится на {self.name} складе")
                        return False
                else:
                    self.store.setdefault(oe.type, [oe])
                self.__current_count += 1
                return True
            else:
                print(f"Склад заполнен. Помещение товара {oe.name} на данный склад не возможно")
        else:
            print("Нельзя поместить пустой объект на склад")

        return False

    def find_in_storage(self, oe):
        """ Ищет объект на складе"""

        for el in self.store[oe.type]:
            if el.name == oe.name:
                return True
        return False

    def get_from_storage(self, oe):
        """ Возвращает объект OfficeEquipment определенного типа\n
            если объект найдет, то возвращает этот объект, и удаляет его со склада
            если объект не найден на складе, то выводит соответствующее сообщение
            :param oe: Объект подкласса OfficeEquipment
            :return obj: Если объект подкласса OfficeEquipment
            :return None: Если объекта нет на складе
        """

        for el in self.store[oe.type]:
            if el.name == oe.name:
                self.store[oe.type].remove(oe)
                self.__current_count -= 1
                return el

        print(f"Товар {oe.name} не найден на складе")

    def remove_from_storage(self, oe):
        """ Удаляет объект со склада совсем. В никуда\n
            :param oe: Объект OfficeEquipment
            :return True: Если удаление прошло удачно
            :return False: Если удаление не получилось
        """
        return self.get_from_storage(oe) is None

    @staticmethod
    def check_object_type(obj, cl):
        """ Проверяет принадлежит ли объект определенному классу
            :param obj: объект
            :param cl: класс
            :return True: если объект принадлежит классу cl
            :return False: если объект не принадлежит классу cl
        """
        return type(obj).__name__ == cl

    @classmethod
    def move_from_to_storage(cls, oe, from_store, to_store):
        """ Переводит товар на другой склад store\n
            :param from_store: Объект класса Storage. Исходный склад
            :param oe: Объект подкласса OfficeEquipment
            :param to_store: Storage object куда перемещаем
            :return True: При удачном перемещение товара
            :return False: При не удачном перемещение товара
        """

        if not cls.check_object_type(from_store, 'Storage'):
            print(f"Объект {from_store} не является Складом")
            return False

        if not cls.check_object_type(to_store, 'Storage'):
            print(f"Объект {to_store} не является Складом")
            return False

        if not from_store.find_in_storage(oe):
            print(f"Объект {oe.name} не нашелся на складе {from_store.name}")
            return False

        to_store.put_in_storage(from_store.get_from_storage(oe))
        return True

    def __str__(self):
        s = f'Товары на складе "{self.name}":\n'
        for e in self.store:
            s += f'{e}:\n'
            for el in self.store[e]:
                s += f'\t{el.name}\n'
        return s


class OfficeEquipment:
    def __init__(self, name, manufacturer, price, t):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.type = t


class Printer(OfficeEquipment):
    def __init__(self, name, manufacturer, price, color, pages):
        super().__init__(name, manufacturer, price, 'printer')
        self.color = color
        self.pages = pages


class Scaner(OfficeEquipment):
    def __init__(self, name, manufacturer, price, color, pages, adf):
        super().__init__(name, manufacturer, price, 'scaner')
        self.color = color
        self.pages = pages
        self.adf = adf


class Xerox(OfficeEquipment):
    def __init__(self, name, manufacturer, price, color, pages):
        super().__init__(name, manufacturer, price, 'xerox')
        self.color = color
        self.pages = pages


# Создание объектов
p1 = Printer('LaserJet 1100N', 'HP', 1200, 'b/w', 24)
p2 = Printer('Canon 1200N', 'Canon', 800, 'color', 10)
s1 = Scaner('Canon super scan 1100N', 'Canon', 300, 'color', 10, 'Yes')
s2 = Scaner('ScanJet 1020', 'HP', 100, 'color', 2, 'No')
x1 = Xerox('OmniCopy 1920', 'Omni', 1000, 'b/w', 40)
x2 = Xerox('Docucenter', 'Xerox', 2000, 'color', 16)

# Создание складов
store1 = Storage('Store One', 14)
store2 = Storage('Store Tow', 10)

# Помещение объектов на склады
store1.put_in_storage(p1)
store1.put_in_storage(s1)
store1.put_in_storage(s2)
store1.put_in_storage(x1)
store2.put_in_storage(x2)
store2.put_in_storage(p2)

# Перенесение одного объекта с одного склада на другой
Storage.move_from_to_storage(p1, store1, store2)

# Списание со склада в никуда
store1.remove_from_storage(s2)

# Сожержание складов
print(store1)
print(store2)

# Проверка полный ли склад
print(store1.is_full)

# Кладем объект p2 на склад.
store1.put_in_storage(p2)

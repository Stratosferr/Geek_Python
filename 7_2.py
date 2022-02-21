from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, cloth_type):
        self.cloth_type = cloth_type

    @abstractmethod
    def print_type(self):
        pass

    @property
    def cloth_type(self):
        return self.__cloth_type

    @cloth_type.setter
    def cloth_type(self, cloth_type):
        if cloth_type == 'suit':
            self.__cloth_type = 'Костюм'
        elif cloth_type == 'coat':
            self.__cloth_type = 'Пальто'
        else:
            self.__cloth_type = cloth_type


class Coat(Cloth):
    def __init__(self, v, cloth_type):
        super().__init__(cloth_type)
        self.v = v

    def print_type(self):
        if self.cloth_type == 'Пальто':
            print(f'На пошив {self.cloth_type} по формуле: Размер/6,5+0,5 необходимо {self.v / 6.5 + 0.5} м. ткани ')
        else:
            print(
                f'Пошив типа {self.cloth_type} не может быть рассчитан, поэтому будет изготовлено Пальто по формуле: Размер/6,5+0,5 необходимо {self.v / 6.5 + 0.5} м. ткани ')


class Suit(Cloth):
    def __init__(self, h, cloth_type):
        super().__init__(cloth_type)
        self.h = h

    def print_type(self):
        print(f'На пошив {self.cloth_type} по формуле: 2*Рост+0,3 необходимо {2 * self.h + 0.3} м. ткани')


a = Coat(65, 'coat')
a.print_type()

b = Suit(130, 'suit')
b.print_type()

с = Coat(122, 'майка')
с.print_type()

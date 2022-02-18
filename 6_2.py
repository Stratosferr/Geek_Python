class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.calc()

    def calc(self):
        print(f"Необходимая масса асфальта {self._length * self._width * 25 * 5 / 1000}тонн")


l = float(input('Длина дороги: '))
w = float(input('Ширина дороги: '))
A = Road(l, w)

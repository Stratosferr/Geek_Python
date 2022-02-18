class Stationery():
    title = 'Stationery'

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки Ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки Карандашем")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки Маркером")


paint = Stationery()
paint.draw()
blue_pen = Pen()
blue_pen.draw()
good_pencil = Pencil()
good_pencil.draw()
red_handle = Handle()
red_handle.draw()

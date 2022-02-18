class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f"Машина {self.name} поехала со скоростью {self.speed} км\ч"

    def stop(self):
        return f"Машина остановилась"

    def turn(self, direction):
        return f"Машина повернула в{direction}"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "машина превышает скорость"
        else:
            return "машина двигается с разрешенной скоростью"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "машина превышает скорость"
        else:
            return "машина двигается с разрешенной скоростью"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(120, "Красный", "Toyota Camry", False)
print(car_1.name)

print(car_1.go())
print(car_1.show_speed())
print(car_1.turn('лево'))
print(car_1.stop())

car_2 = WorkCar(45, "Зеленый", "Газель", False)
print(car_2.name)
print(car_2.go())
print(car_2.show_speed())
print(car_2.turn('лево'))
print(car_2.stop())

car_3 = PoliceCar(120, "Белый", "Toyota", True)
print(car_3.name)
print(car_3.go())
print(car_3.show_speed())
print(car_3.turn('право'))
print(car_3.stop())

car_4 = SportCar(100, "Зеленый", "Lamborgini", False)
print(car_4.name)
print(car_4.go())
print(car_4.show_speed())
print(car_4.turn('лево'))
print(car_4.stop())

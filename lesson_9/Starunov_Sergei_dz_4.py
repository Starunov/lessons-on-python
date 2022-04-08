class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} - движение началось'

    def stop(self):
        return f'{self.name} - движение прекращено'

    def turn(self, direction):
        return f'{self.name} - движение {direction}'

    def show_speed(self):
        return f'текущая скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Слишком высокая скорость')
        return f'текущая скорость {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Слишком высокая скорость')
        return f'текущая скорость {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


if __name__ == '__main__':
    from random import choice

    cars = [
        TownCar(61, 'light brown', 'BMW'),
        SportCar(251, 'red', 'Lada 21093'),
        WorkCar(41, 'yellow', 'K700', is_police=True),
        PoliceCar(35, 'blue and white', 'Skoda Octavia')
    ]
    for car in cars:
        print('Атрибуты:')
        print(car.speed, car.color, car.name, car.is_police, sep=' | ')
        print('Методы:')
        print(car.go())
        print(car.stop())
        print(car.turn(choice(['налево', 'направо', 'вперед', 'назад', 'вверх', 'вниз'])))
        print(car.show_speed())
        print('='*50)

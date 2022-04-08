class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} выделяет')


if __name__ == '__main__':
    parent = Stationery('Карцелярка')
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    parent.draw()
    pen.draw()
    pencil.draw()
    handle.draw()

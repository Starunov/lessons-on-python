from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_quantity_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def get_quantity_cloth(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def get_quantity_cloth(self):
        return 2 * self.height + 0.3


if __name__ == '__main__':
    coat = Coat('Пальто', 52)
    print(coat.get_quantity_cloth)
    suit = Suit('Костюм', 170)
    print(suit.get_quantity_cloth)
    print('Общий расход ткани:', suit.get_quantity_cloth + coat.get_quantity_cloth)

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt(self, coating_thickness=1, expense=25):
        """
        :param coating_thickness: Толщина покрытия (в сантиметрах)
        :param expense: Масса материала на один кв.метр (в кг) при толщине покрытия в 1 см
        :return: Необходимая масса материала (в тоннах), для покрытия всей дороги
        """
        return int((self._width * self._length * coating_thickness * expense) / 1000)


if __name__ == '__main__':
    road = Road(5000, 20)
    print(road.calc_asphalt(5))

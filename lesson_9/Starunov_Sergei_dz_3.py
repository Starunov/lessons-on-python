class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int and float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return round(self._income['wage'] + self._income['wage']*self._income['bonus'], 2)


if __name__ == '__main__':
    locksmith = Position('Иван', 'Иванов', 'Слесарь 18 разряда', 150000, 0.4)
    driver = Position('Валера', 'Валерьев', 'Водитель категории С', 40231.99, 0.15)
    print(locksmith.get_full_name(), locksmith.get_total_income(), sep=' | ')
    print(driver.get_full_name(), driver.position, driver.get_total_income(), sep=' | ')

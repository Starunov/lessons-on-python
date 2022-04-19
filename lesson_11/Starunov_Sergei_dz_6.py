# Task 4, 5, 6

from pprint import pprint
from random import randint


class WareHouse:
    __office_device = {}

    def is_available(self, device):
        """Проверяет доступность техники на складе"""
        type_device = device.__class__.__name__.lower()
        brand = device.brand.lower()
        model = device.model.lower()
        try:
            self.__office_device[type_device][brand][model]
        except KeyError as ex:
            print(f'{ex} is not defined')
            return False
        else:
            return True

    @property
    def get_all_devices(self):
        return self.__office_device

    def get_list_devices(self, type_device, condition):
        """Возвращает список устройств, удовлетворяющих переданному параметру condition"""
        list_devices = []
        dev = map(lambda x: (x[0], x[1].items()), self.__office_device[type_device].items())
        for brand, (list_models) in dev:
            for model, [count, *param] in list_models:
                if condition in param:
                    list_devices.append({brand: {model: [count] + param}})
        return list_devices

    def upload_to_warehouse(self, device, quantity: int = 1):
        try:
            int(quantity)
        except ValueError as err:
            raise ValueError(f'{err}: необходимо ввести целое число для указания количества техники')
        type_device = device.__class__.__name__.lower()
        brand = device.brand.lower()
        model = device.model.lower()
        param = device.param

        if self.__office_device.get(type_device) is None:
            self.__office_device.setdefault(type_device, {brand: {model: [quantity] + param}})
        elif self.__office_device.get(type_device).get(brand) is None:
            self.__office_device[type_device].setdefault(brand, {model: [quantity] + param})
        elif self.__office_device[type_device][brand].get(model) is None:
            self.__office_device[type_device][brand].setdefault(model, [quantity] + param)
        else:
            self.__office_device[type_device][brand][model][0] += quantity

    def take_from_warehouse(self, device, quantity: int = 1):
        try:
            int(quantity)
        except ValueError as err:
            raise ValueError(f'{err}: необходимо ввести целое число для указания количества техники')
        type_device = device.__class__.__name__.lower()
        brand = device.brand.lower()
        model = device.model.lower()
        count = self.__office_device[type_device][brand][model][0]
        if count < quantity:
            raise ValueError('На складе меньше элементов, чем было запрошено')
        elif count == quantity:
            self.__office_device[type_device][brand].pop(model)
        else:
            self.__office_device[type_device][brand][model][0] -= quantity


class OfficeTechnic:
    def __init__(self, brand, model, *args):
        self._brand = brand
        self._model = model
        self._param = list(args)

    @property
    def brand(self):
        if type(self._brand) != str:
            raise ValueError(f'brand {self._brand}: must be format "str"')
        return self._brand

    @property
    def model(self):
        if type(self._model) != str:
            raise ValueError(f'model {self._model}: must be format "str"')
        return self._model

    @property
    def param(self):
        for p in self._param:
            if type(p) != str:
                raise ValueError(f'parameters {p} the device {self._brand} {self._model}: must be format "str"')
        return self._param


class Printer(OfficeTechnic):
    def __init__(self, brand, model, *args):
        super().__init__(brand, model, *args)


class Scanner(OfficeTechnic):
    def __init__(self, brand, model, *args):
        super().__init__(brand, model, *args)


class Copier(OfficeTechnic):
    def __init__(self, brand, model, *args):
        super().__init__(brand, model, *args)


if __name__ == '__main__':
    storage = WareHouse()

    printers = [
        Printer('Cannon', '250i', 'струйный', 'old_model'),
        Printer('Cannon', 'lbp6020', 'лазерный', 'new_model'),
        Printer('HP', 'p1102', 'лазерный', 'A0'),
        Printer('HP', 't730', 'струйный', 'reliable')
    ]

    scanners = [
        Scanner('Epson', '12000XL', 'планшетный'),
        Scanner('Epson', 'ES-580W', 'потоковый'),
        Scanner('Cannon', 'P-215II', 'протяжной'),
    ]

    copiers = [
        Copier('HP', 'c7183', 'мфу'),
        Copier('HP', 'f370', 'мфу')
    ]

    for printer in printers:
        storage.upload_to_warehouse(printer, quantity=randint(1, 5))
    for scaner in scanners:
        storage.upload_to_warehouse(scaner, quantity=randint(1, 5))
    for copier in copiers:
        storage.upload_to_warehouse(copier, quantity=randint(1, 5))

    pprint(storage.get_all_devices)
    print()
    storage.take_from_warehouse(printers[0], 2)
    storage.is_available(printers[0])
    print(storage.get_list_devices('printer', 'струйный'))
    print()
    pprint(storage.get_all_devices)

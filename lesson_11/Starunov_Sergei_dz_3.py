class NotANumber(Exception):
    __value = ''
    __result = []

    def __init__(self, value):
        self.__value = value
        self.is_number()

    def is_number(self):
        try:
            NotANumber.__result.append(int(self.__value))
        except ValueError:
            print(f'{self.__value} is not a number')

    @classmethod
    def get_list(cls):
        return cls.__result


if __name__ == '__main__':
    while True:
        enter = input('Enter number > ')
        if enter == 'stop':
            break
        NotANumber(enter)

    print(NotANumber.get_list())

class MyDivisionByZero(Exception):
    def __str__(self):
        return 'деление на ноль'


if __name__ == '__main__':
    divisible = int(input('Divisible: '))
    divider = int(input('Divider: '))

    if divider == 0:
        raise MyDivisionByZero
    print(divisible / divider)

from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('call function with parameters: ', func.__name__, '(', sep='', end='')
        end = ', ' if kwargs else ''  # для красоты вывода
        print(*map(lambda x: f'{x}: {type(x)}', args), sep=', ', end=end)
        print(*map(lambda dictionary: f'{dictionary[0]}={dictionary[1]}: {type(dictionary[1])}', kwargs.items()),
              sep=', ', end='')
        print(')')
        calc_cube = func(*args, **kwargs)
        print(f'return value {calc_cube}: {type(calc_cube)}')
        return calc_cube
    return wrapper


@logger
def calc_degree(*args: int, degree=3):
    if len(args) > 1:
        return tuple([num ** degree for num in args])
    return args[0] ** degree


print(
    f'Результат работы функции {calc_degree.__name__}:', calc_degree(3, 8, 9, degree=2)
)  # результат работы функции wrapper ... (такой вывод без декоратора wraps)

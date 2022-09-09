from functools import wraps


def val_checker(func_validator):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not func_validator(*args):
                raise ValueError('wrong parameters on input:', *args)
            return func(*args)
        return wrapper
    return _val_checker


@val_checker(lambda x: x.isdigit())
def type_str_to_int(string: str.isdigit):
    """Преобразует число в строковом типе в число типа int"""
    return int(string)


print(type_str_to_int('22'), type_str_to_int.__name__)

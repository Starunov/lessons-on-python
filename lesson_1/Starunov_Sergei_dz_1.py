def count_time_interval(duration):
    # day, hour = divmod(duration, 86400)
    # hour, minute = divmod(hour, 3600)
    # minute, second = divmod(minute, 60)

    day = duration // 86400
    hour = duration % 86400 // 3600
    minute = duration % 86400 % 3600 // 60
    second = duration % 86400 % 3600 % 60

    if day:
        result = f'{day} дн {hour} час {minute} мин {second} сек'
    elif hour:
        result = f'{hour} час {minute} мин {second} сек'
    elif minute:
        result = f'{minute} мин {second} сек'
    else:
        result = f'{second} сек'

    return result


values = [53, 153, 4153, 400153]
for val in values:
    print(count_time_interval(val))

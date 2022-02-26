def sum_digits(number):
    """
    Суммирует цифры числа
    :param number: Целое положительное число
    :return: Сумма цифр числа
    """
    res = 0
    while number != 0:
        res += number % 10  # Прибавить крайнюю цифру к результату
        number = number // 10  # Убрать крайнюю цифру из числа
    return res


numbers_three_degrees = []
sum_el1 = 0
sum_el2 = 0

for num in range(1000):
    if num % 2:
        numbers_three_degrees.append(num ** 3)
        sum_el1 += num ** 3 if not sum_digits(num ** 3) % 7 else 0
        sum_el2 += num**3 + 17 if not sum_digits(num**3 + 17) % 7 else 0

print(numbers_three_degrees)
print(sum_el1)
print(sum_el2)




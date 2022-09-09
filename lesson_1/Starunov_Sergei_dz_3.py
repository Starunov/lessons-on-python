def word_declension(number):
    if 10 < number % 100 < 15:  # 11, 12, 13, 14
        return 'процентов'
    elif number % 10 == 1:  # 1
        return 'процент'
    elif 1 < number % 10 < 5:  # 2, 3, 4
        return 'процента'
    else:  # остальные значения
        return 'процентов'


for i in range(1, 101):
    print(i, word_declension(i))

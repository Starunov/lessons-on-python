from random import choice, shuffle

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num: int, dont_repeat=False):
    """
    Формирует шутки случайным выбором из списков существительных, наречий и прилагательных
    :param num: Количество шуток
    :param dont_repeat: Флаг, разрешающий или запрещающий повторы слов в шутках
    :return: Список с шутками
    """
    jokes_list = []
    for i in range(num):
        if not (nouns and adverbs and adjectives):  # Формировать шутки пока какой-нибудь из списков не станет пустым
            break
        if dont_repeat:
            # Перемешиваем списки
            shuffle(nouns)
            shuffle(adverbs)
            shuffle(adjectives)
            jokes_list.append(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')
        else:
            jokes_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return jokes_list


print(get_jokes(78, dont_repeat=True))

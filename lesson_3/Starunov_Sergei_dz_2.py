eng_rus = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(numeral: str):
    if numeral.lower() not in eng_rus:
        return
    # Иначе
    return eng_rus[numeral.lower()].title() if numeral.istitle() else eng_rus[numeral.lower()]


numerals = ['one', 'Red', 'Three', 'ten', 'Nine', 'eight']
print(*map(num_translate_adv, numerals))

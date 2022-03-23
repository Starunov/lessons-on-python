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


def num_translate(numeral: str.lower):
    return eng_rus[numeral] if numeral in eng_rus else None


numerals = ['one', 'red', 'three', 'ten', 'nine', 'eight']
print(*map(num_translate, numerals))

import re

# При многократном использовании в скрипте, есть смысл сохранить регулярное выражение в переменную методом re.compile()
RE_EMAIL = re.compile(
        r'(?P<username>\b(?:[^\.\s])*[\w\S]*(?:[^\.\s]))@(?P<domain>([^\W][\w.-]*[^\W])\.[A-Za-z]{2,}$)')


def email_parse(email):
    """
    :param email: abcdefj@mail.ru
    :return: dict ==> {'username': 'abcdefj', 'domain': 'mail.ru'}
    """
    res_iter = RE_EMAIL.match(email)  # См. Match.groupdict(default=None)
    if not res_iter:
        raise ValueError(f'wrong email: {email}')
    return res_iter.groupdict()


email_list = [
    # валидные
    'a@mail.com',
    'aspir@sau.ru',
    'antan@sfgau.ru',
    'axo@yandex.ru',
    'kipres@bk.ru',
    'arkhipov@sjhu.ru',
    'asl_anov_vs@mail.ru',
    'aslanov@ffds.ru',
    'byui@yandex.ru',
    'balykin@rambler.ru',
    'okm@ssau.ru',
    'bogdanovich@ssau.ru',
    'bolgova.vv@tttt.tttttttttt-tttttttt.ru',
    'rud@ssau.ru',
    # инвалидные
    'gareyev@ssauru',
    'boris.ru',
    'careerssau.ru',
    '.abukhanko@mail.ru',
    'usovet.@ssau.ru',
    'vas hukov@ssau.ru',
    'nirs@ssau.',
    'veshagina@ssau.r',
    'v ',
    'voronova.ov@ssau.45',
    'gavrilov@ssau.ru7',
]

for eml in email_list:
    print(email_parse(eml))

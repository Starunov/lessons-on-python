from requests import get

TAG_VALUE = '<Value>'
TAG_CLOSE_VALUE = '</Value>'
TAG_NOMINAL = '<Nominal>'
TAG_CLOSE_NOMINAL = '</Nominal>'


def currency_rates(currency_code):
    """
    Принимает код валюты в формате str: 'USD', 'EUR' ...
    Возвращает курс валюты по отношению к рублю в формате float
    """
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    currency_code = currency_code.upper()  # Приведение символов к верхнему регистру
    response = get(url)  # Получаем ответ от сервера в переменную response
    if response.status_code != 200:  # 200 - запрос выполнен успешно
        print('Ошибка выполнения запроса!')
        return

    text = response.text  # ответ в виде текста html
    if currency_code not in text:
        return
    text = text[text.find(currency_code):]  # Находим в тексте код валюты и получаем срез от текста начиная с этого кода
    # Делим оставшийся текст по тегам и получаем нужный фрагмент текста. Меняем запятую на точку, чтобы сделать float
    value = float(text.split(TAG_VALUE)[1].split(TAG_CLOSE_VALUE)[0].replace(',', '.'))
    nominal = int(text.split(TAG_NOMINAL)[1].split(TAG_CLOSE_NOMINAL)[0])

    return value / nominal


print(currency_rates('usd'))
print(currency_rates('eur'))

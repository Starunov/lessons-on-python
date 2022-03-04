from requests import get
from datetime import datetime, timedelta

TAG_VALUE = '<Value>'
TAG_CLOSE_VALUE = '</Value>'
TAG_NOMINAL = '<Nominal>'
TAG_CLOSE_NOMINAL = '</Nominal>'
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'


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
    # В ответе сервера response также имеется словарь headers, который содержит доп. информацию
    date_response = datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z') + timedelta(hours=3)  # utc+3 МСК
    date_str = date_response.strftime('%d.%m.%Y')  # тип строка в формате дд.мм.гггг
    text = response.text
    if currency_code not in text:
        return
    text = text[text.find(currency_code):]
    value = float(text.split(TAG_VALUE)[1].split(TAG_CLOSE_VALUE)[0].replace(',', '.'))
    nominal = int(text.split(TAG_NOMINAL)[1].split(TAG_CLOSE_NOMINAL)[0])

    return value / nominal, date_str


print(currency_rates('usd'))

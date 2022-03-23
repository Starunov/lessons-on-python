import utils

currency_list = ['usd', 'EUR', 'kzt', 'aud', 'rub', 'BYN']
for item in currency_list:
    print(utils.currency_rates(item))

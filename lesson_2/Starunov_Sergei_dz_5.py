price_list = [15.23, 56.85, 78.56, 13.8, 0.15, 2.23, 9.99, 12.2, 99.99, 123.01, 0.0, 142.12, 36.6, 6.11, 6.11, 25.25]
print('Начальный список: ', price_list)
print('ID начального списка:', id(price_list), end='\n\n')

# A
print('A:', end=' ')
for price in price_list:
    rub = int(price)
    kop = int(price * 100 - rub * 100)
    print(f'{rub} руб {kop:02d} коп', end=', ')
print()

# B
print('B:', end=' ')
price_list.sort()
print('Список цен по возрастанию: ', price_list, end='\n   ')
print('ID списка отсортированного по возрастанию:', id(price_list))

# C
print('C:', end=' ')
list_desc_order = sorted(price_list, reverse=True)
print('Список цен по убыванию: ', list_desc_order, end='\n   ')
print('ID списка отсортированного по убыванию:', id(list_desc_order))

# D
print('D:', end=' ')
print('Топ 5 дорогих товаров по возрастанию: ', end='')
print(*price_list[-5:], sep=', ')

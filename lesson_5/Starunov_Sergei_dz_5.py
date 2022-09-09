"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 10, 7, 4, 11]

# Using dict()
# tmp = {}
# for num in src:
#     if tmp.get(num):
#         tmp[num] += 1
#     else:
#         tmp[num] = 1
#
# result = [key for key in tmp if tmp[key] == 1]
# print(result)


# Using set()
duplicate_el = set()
tmp = set()
for num in src:
    duplicate_el.add(num) if num in tmp else tmp.add(num)

result = [el for el in src if el not in duplicate_el]
print(result)

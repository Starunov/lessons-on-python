from time import perf_counter
from sys import getsizeof

""" Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#  for in
start = perf_counter()
result = []
prev_el = src[0]
for el in src:
    if el > prev_el:
        result.append(el)
    prev_el = el
stop = perf_counter()
print('Using "for in":', *result, '\nTime execution:', stop - start, '\nSize result:', getsizeof(result), '\n')
# ======================================================================================================================
#  List Comprehension
start = perf_counter()
result = [num for i, num in enumerate(src[1:]) if num > src[i]]
stop = perf_counter()
print('Using "List comprehension":', *result, '\nTime execution:', stop - start, '\nSize result:', getsizeof(result), '\n')

#  Генератор
start = perf_counter()
result = (num for i, num in enumerate(src[1:]) if num > src[i])
stop = perf_counter()
print('Using "generator":', *result, '\nTime execution:', stop - start, '\nSize result:', getsizeof(result), '\n')
# ======================================================================================================================
#  Функции: filter, map
start = perf_counter()
result = filter(lambda x: x, map(lambda prev, cur: cur if cur > prev else None, src, src[1:]))
stop = perf_counter()
print('Using "filter, map":', *result, '\nTime execution:', stop - start, '\nSize result:', getsizeof(result), '\n')

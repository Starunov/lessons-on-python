def odd_nums(number: int):
    for elem in range(1, number + 1, 2):
        yield elem


gen = odd_nums(15)
for num in gen:
    print(num)

print(next(gen))  # StopIteration

def odd_nums(number: int):
    return (elem for elem in range(1, number + 1, 2))


gen = odd_nums(15)
for num in gen:
    print(num)

print(next(gen))  # StopIteration

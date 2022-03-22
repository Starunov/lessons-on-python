tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Юрий', 'Леонид',
]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen_assign_tutor():
    return ((name, klasses[i]) if i < len(klasses) else (name, None) for i, name in enumerate(tutors))


gen = gen_assign_tutor()
print(type(gen))
for items in gen:
    print(items)

print(next(gen))  # StopIteration

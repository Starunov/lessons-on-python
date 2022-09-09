def thesaurus(*args, key_sort=False):
    names_dict = {}
    if key_sort:
        args = sorted(args)

    for name in args:
        names_dict.setdefault(name[0], list(filter(lambda x: x[0] == name[0], args)))
    return names_dict


staff_list = ['Сергей', 'Егор', 'Максим', 'Елена', 'Михаил', 'Семен', 'Яна', 'Гриша', 'Андрей', 'Александр']
print(thesaurus(*staff_list, key_sort=True))

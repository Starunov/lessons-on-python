def thesaurus_adv(*args, key_sort=False):
    """
    Принимает аргументы типа 'строка' в виде 'Имя Фамилия'
    Возвращает словарь в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
    начинающиеся с соответствующей буквы
    """
    actors_dict = {}
    if key_sort:
        args = sorted(args, key=lambda x: x.split()[1])  # Сортируем args по фамилии

    for full_name in args:
        first_name, last_name = full_name.split()
        if actors_dict.get(last_name[0]) is None:
            actors_dict.setdefault(last_name[0], {first_name[0]: [full_name]})
        elif actors_dict[last_name[0]].get(first_name[0]) is None:
            actors_dict[last_name[0]].setdefault(first_name[0], [full_name])
        else:
            actors_dict[last_name[0]][first_name[0]].append(full_name)
    return actors_dict


actors_list = ['Сергей Бурунов',
               'Екатерина Гусева',
               'Константин Хабенский',
               'Светлана Ходченкова',
               'Данила Козловский',
               'Владимир Машков',
               'Екатерина Климова',
               'Сергей Безруков',
               'Оксана Акиньшина',
               'Владимир Вдовиченков',
               'Елена Яковлева',
               'Марина Александрова',
               'Татьяна Арнтгольц',
               'Настасья Самбурская'
               ]
print(thesaurus_adv(*actors_list, key_sort=True))

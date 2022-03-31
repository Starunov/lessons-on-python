from itertools import zip_longest


def gen_user_hobby(users_file, hobby_file):
    with open(users_file, encoding='utf-8') as f_users, open(hobby_file, encoding='utf-8') as f_hobby:
        user_list = [u.replace('\n', '') for u in f_users]
        hobby_list = [h.replace('\n', '') for h in f_hobby]
        if len(user_list) > len(hobby_list):
            for user, hobby in zip_longest(user_list, hobby_list):
                yield user, hobby
        else:
            for user, hobby in zip(user_list, hobby_list):
                yield user, hobby


if __name__ == '__main__':
    import sys
    from os.path import exists
    if exists(sys.argv[1]) and exists(sys.argv[2]):  # Проверка наличия входных файлов
        users = sys.argv[1]
        hobby = sys.argv[2]
    else:
        print('Incorrect input parameters: file_name_users, file_name_hobby, resulting_file_name')
        raise SystemExit(1)
    result = sys.argv[3]

    users_hobby = gen_user_hobby(users, hobby)
    with open(result, 'w', encoding='utf-8') as f:
        print(*map(lambda x: f"{x[0]}: {x[1]}", users_hobby), sep='\n', file=f)

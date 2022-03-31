import json

with open('users.csv', encoding='utf-8') as f_users:
    user_list = [line.replace('\n', '') for line in f_users.readlines()]

with open('hobby.csv', encoding='utf-8') as f_hobby:
    hobby_list = [line.replace('\n', '') for line in f_hobby.readlines()]

if len(hobby_list) > len(user_list):
    raise SystemExit(1)

users_hobby = dict((user, hobby_list[i]) if i < len(hobby_list) else (user, None) for i, user in enumerate(user_list))

with open('users_hobby.csv', 'w', encoding='utf-8') as f:
    json.dump(users_hobby, f)
# {"\u0418\u0432\u0430\u043d\u043e\u0432,\u0418\u0432\u0430\u043d,\u0418\u0432\u0430\u043d\u043e\u0432\u0438\...}

with open('users_hobby.csv', encoding='utf-8') as f:
    file_data = json.load(f)  # Загруженные данные из файла, тип - словарь

print(file_data)  # type ==> dict

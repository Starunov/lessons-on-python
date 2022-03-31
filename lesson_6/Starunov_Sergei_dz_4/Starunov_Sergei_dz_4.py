from itertools import zip_longest


def gen_user_hobby():
    with open('users.csv', encoding='utf-8') as f_users, open('hobby.csv', encoding='utf-8') as f_hobby:
        user_list = [u.replace('\n', '') for u in f_users]
        hobby_list = [h.replace('\n', '') for h in f_hobby]
        if len(user_list) > len(hobby_list):
            for user, hobby in zip_longest(user_list, hobby_list):
                yield user, hobby
        else:
            for user, hobby in zip(user_list, hobby_list):
                yield user, hobby


users_hobby = gen_user_hobby()
with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    print(*map(lambda x: f"{x[0]}: {x[1]}", users_hobby), sep='\n', file=f)

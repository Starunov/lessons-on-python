import re

#                              ↓   IP  ↓        ↓  date   ↓      ↓ type ↓  ↓resour↓             ↓cod↓  ↓siz↓
RE_PARSE_FILE = re.compile(r'\A([\w.:]+)[\s-]+\[([\w/: +]+)\]\s\"([A-Z]+)\s([\w/]+)\s[\w/.\"]+\s(\d+)\s(\d+)')


def gen_data():
    with open('nginx_logs.txt', encoding='utf-8') as file:
        for string in file.readlines():
            yield string


with open('result_task_2.txt', 'w', encoding='utf-8') as file:
    for line in gen_data():
        m = RE_PARSE_FILE.match(line)
        print(str(m.groups()), file=file)

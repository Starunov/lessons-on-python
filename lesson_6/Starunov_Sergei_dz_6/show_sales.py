import sys

def main(argv):
    """
    :param argv: Параметры командной строки (начальная и конечная строки считывания файла
    :return: Строки согласно параметрам. Все строки в случае если параметры не заданы
    """
    with open('bakery.csv', encoding='utf-8') as file:
        if len(argv) == 1:
            return [line.replace('\n', '') for line in file]
        if len(argv) == 2:
            return [line.replace('\n', '') for i, line in enumerate(file) if i+1 >= int(argv[1])]
        elif len(argv) == 3:
            return [line.replace('\n', '') for i, line in enumerate(file) if int(argv[1]) <= i + 1 <= int(argv[2])]


if __name__ == '__main__':
    print(*main(sys.argv), sep='\n')

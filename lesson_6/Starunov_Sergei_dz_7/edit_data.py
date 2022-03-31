import sys

def main(argv):
    if len(argv) < 3:
        print('Missing parameters. Need two parameters: entry_number and new_value')
        raise SystemExit()

    number_line = argv[1]
    new_value = argv[2]

    if not (number_line.isdigit() and new_value.replace('.', '', 1).isdigit()):
        print('Incorrect input parameters. Must be numbers')
        raise SystemExit()

    with open('bakery.csv', 'r', encoding='utf-8') as file:
        read_file = [new_value + '\n' if i == int(number_line) - 1 else line for i, line in enumerate(file)]
        if int(number_line) > len(read_file):
            print('Data cannot be changed')
            raise SystemExit()

    with open('bakery.csv', 'w', encoding='utf-8') as file:
        for line in read_file:
            file.write(line)


if __name__ == '__main__':
    main(sys.argv)



import sys

def main(argv):
    price = argv[1] if argv[1].replace('.', '', 1).isdigit() else None
    if price:
        with open('bakery.csv', 'a', encoding='utf-8') as file:
            print(price, file=file)


if __name__ == '__main__':
    main(sys.argv)

class ComplexNum:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __str__(self):
        return str(self.complex_num)

    def __add__(self, other):
        return ComplexNum(self.complex_num + other.complex_num)

    def __mul__(self, other):
        return ComplexNum(self.complex_num * other.complex_num)


if __name__ == '__main__':
    n1 = ComplexNum(4 + 5j)
    n2 = ComplexNum(4 + 55j)
    print(n1)
    print(n2)
    print(n1 + n2)
    print(n1 * n2)

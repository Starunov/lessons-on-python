def pretty_out(matrix: list):
    output = ''
    for row in matrix:
        for column in row:
            output += f'{column}' if column == row[-1] else f'{column} '
        if not (row == matrix[-1]):
            output += '\n'
    return output


class Matrix:
    def __init__(self, array: list):
        self.array = array
        self.is_correct()

    def __str__(self):
        return pretty_out(self.array)

    def __add__(self, other):
        if len(self.array) != len(other.array):
            raise ValueError('The sizes of the matrices are not equal!')
        for row1, row2 in zip(self.array, other.array):
            if len(row1) != len(row2):
                raise ValueError('The sizes of the matrices are not equal!')
        result = []
        for i, (row1, row2) in enumerate(zip(self.array, other.array)):
            result.append([])
            for val1, val2 in zip(row1, row2):
                result[-1].append(val1 + val2)
        return result

    def is_correct(self):
        if type(self.array) != list:
            raise ValueError('the input argument must be a list')
        if not len(self.array):
            raise ValueError('The list should not be empty')
        if type(self.array[0]) != list:
            raise ValueError('The input argument should be a list of lists')
        one_elem_size = len(self.array[0])
        for elem in self.array:
            if len(elem) != one_elem_size:
                raise ValueError('There are not equal number of elements in the rows of the matrix')


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 3], [7, 8, 9], [1, 5, -9]])
    matrix2 = Matrix([[1, 2, 4], [1, 2, 3], [5, 7, 8]])
    print('matrix1')
    print(matrix1)
    print('matrix2')
    print(matrix2)
    print('sum matrix1 and matrix2')
    print(pretty_out(matrix1 + matrix2))

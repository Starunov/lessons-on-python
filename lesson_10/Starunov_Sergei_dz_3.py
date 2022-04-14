class Cell:
    def __init__(self, quantity_cells: int):
        self.quantity_cells = quantity_cells

    def __add__(self, other):
        return self.quantity_cells + other.quantity_cells

    def __sub__(self, other):
        if self.quantity_cells - other.quantity_cells > 0:
            return self.quantity_cells - other.quantity_cells
        return 'Результат меньше или равно нулю'

    def __mul__(self, other):
        return self.quantity_cells * other.quantity_cells

    def __floordiv__(self, other):  # Целочисленное деление
        return self.quantity_cells // other.quantity_cells

    def __truediv__(self, other):  # Деление x/y
        return self.quantity_cells / other.quantity_cells

    def make_order(self, cells_in_row):
        parts, remains = divmod(self.quantity_cells, cells_in_row)
        return '\\n'.join(['*' * cells_in_row] * parts + (['*' * remains] if remains else []))


if __name__ == '__main__':
    cell_1 = Cell(12)
    cell_2 = Cell(12)
    print(cell_1)
    print(cell_2)
    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print(cell_1 * cell_2)
    print(cell_1 // cell_2)
    print(cell_1 / cell_2)
    print(cell_2.make_order(5))

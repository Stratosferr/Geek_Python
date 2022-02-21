class Matrix():
    def __init__(self, matrix):
        if isinstance(matrix, list):
            self.matrix = matrix
            self.max_rows = len(self.matrix)
            self.max_columns = max([len(matrix[i]) for i in range(len(matrix))])
        else:
            print(f'Input data is not matrix, it is {type(matrix)}')

    def __str__(self):
        return str('\n'.join(['\t'.join([str(num) for num in row]) for row in self.matrix]))

    def __add__(self, other):
        self.max_columns = max(max(len(i) for i in self.matrix), max([len(j) for j in other.matrix]))
        self.max_rows = max(len(self.matrix), len(other.matrix))
        self.matrix.extend([[0] * (self.max_columns) for _ in range(self.max_rows - len(self.matrix))])
        other.matrix.extend([[0] * (self.max_columns) for _ in range(self.max_rows - len(other.matrix))])
        for i in range(len(self.matrix)):
            self.matrix[i].extend([0] * (self.max_columns - len(self.matrix[i])))
            other.matrix[i].extend([0] * (self.max_columns - len(other.matrix[i])))
        self.result_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.max_columns)] for i in
                              range(self.max_rows)]
        return Matrix(self.result_matrix)


matrix_1 = Matrix([[1, 2], [1, 2, 3, 6], [4, 5, 6], [1, 1, 1]])
matrix_2 = Matrix([[1, 2, 6, 7, 9], [1, 2, 3, 6], [2, 2, 3], [4, 5, 3]])
matrix_3 = Matrix([[1, 1, 1, 1, 2], [3, 6], [4, 6, 3]])

print(matrix_1 + matrix_2 + matrix_3)

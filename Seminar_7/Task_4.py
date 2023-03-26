class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = []
        for row in self.data:
            result.append(' '.join([str(k) for k in row]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.data) == len(other.data):
            result = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
                      for i in range(len(self.data))]
            return Matrix(result)
        else:
            return


matrix1_class = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2_class = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix3_class = matrix1_class + matrix2_class

print(matrix1_class, end='\n\n')
print(matrix2_class, end='\n\n')
print(matrix3_class)

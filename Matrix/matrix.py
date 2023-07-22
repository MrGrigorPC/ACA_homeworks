def check_row_of_matrix(list) -> int:
    m = len(list)
    n = len(list[0])
    for i in range(m):
        if len(list[i]) != n:
            raise ValueError(
                'Non correct format of matrix, all the rows need to be equal')
    return m, n


class Matrix:
    def __init__(self, inp_list):
        # Check all the rows in matrix have the same size
        try:
            self.m, self.n = check_row_of_matrix(inp_list)
        except:
            raise ValueError('Non correct format of matrix')
        self.matrix = inp_list

    def __str__(self) -> str:
        arr = [list(map(str, i)) for i in self.matrix]
        result = ''
        for i in range(self.m):
            result += ' '.join(arr[i]) + '\n'
        return result

    def __add__(self, other):
        result = []
        if self.m == other.m and self.n == other.n:
            result = [[0 for j in range(self.n)] for i in range(self.m)]
            for i in range(self.m):
                for j in range(self.n):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        else:
            raise ValueError(
                'Two matrices need to have the same dimensions for addition operation')
        return Matrix(result)

    def __sub__(self, other):
        result = []
        if self.m == other.m and self.n == other.n:
            result = [[0 for j in range(self.n)] for i in range(self.m)]
            for i in range(self.m):
                for j in range(self.n):
                    result[i][j] = self.matrix[i][j] - other.matrix[i][j]
        else:
            raise ValueError(
                'Two matrices need to have the same dimensions for addition operation')
        return Matrix(result)

    def __mul__(self, other):
        result = []
        try:
            if type(other) == int or isinstance(other, Matrix):
                result = [[0 for j in range(self.n)] for i in range(self.m)]
                for i in range(self.m):
                    for j in range(self.n):
                        if type(other) == int:
                            result[i][j] = self.matrix[i][j] * other
                        elif isinstance(other, Matrix) and self.m == other.m and self.n == other.n:
                            result[i][j] += self.matrix[i][j] * other.matrix[i][j]
                        else:
                            raise ValueError('Unexpected type')
            return Matrix(result)
        except:
            raise ValueError('Second operand must be matrix or number')

    def __matmul__(self, other):
        result = []
        if self.n == other.m:
            m, n = self.m, other.n
            result = [[0 for j in range(n)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    for k in range(self.n):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

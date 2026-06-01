"""Matrix Class

A re-write of previous code to convert previous matrix functions into
an object-oriented program

"""

m: type = list[list[float]]


class Matrix:
    def __init__(self, matrix: m) -> None:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix):
            raise TypeError("Matrix does not support comparison against other types")

        return self.rows == other.rows and self.cols == other.cols

    def add_matrix(self, other: Matrix, coeff=1) -> None:
        if not self:
            raise TypeError("Matrices need to be the same dimensions")

        for row in range(self.rows):
            for col in range(self.cols):
                self.matrix[row][col] += other.matrix[row][col] * coeff

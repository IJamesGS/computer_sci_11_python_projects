"""Matrix Class

A re-write of previous code to convert previous matrix functions into
an object-oriented program

"""

from __future__ import annotations

import random

from matrix_solver_v2 import elimination

type M = list[list[float]]


class Matrix:
    # ---- Initializers ----

    def __init__(self, matrix: list[list[float]]) -> None:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.row_vectors = self.matrix
        self.column_vectors = list(zip(*matrix))
        if self.rows == self.cols:
            self.square = True

        else:
            self.square = False

    @staticmethod
    def create_random_matrix(cols, rows, cell_min, cell_max) -> Matrix:

        in_matrix: M = []

        for n in range(rows):
            in_matrix.append([])
            for _ in range(cols):
                in_matrix[n].append(random.uniform(cell_min, cell_max))

        return Matrix(in_matrix)

    @staticmethod
    def create_identity(size: int) -> Matrix:
        if size < 1:
            raise ValueError("Matrix must have dimensions greater than 0.")

        identity: M = []

        for row in range(size):
            identity.append([])
            for column in range(size):
                if row == column:
                    identity[row].append(1)

                else:
                    identity[row].append(0)

        return Matrix(identity)

    # ---- Dunder Methods ----

    def __eq__(self, other) -> bool:
        if not isinstance(other, Matrix):
            raise TypeError("Matrix does not support comparison against other types")

        return self.rows == other.rows and self.cols == other.cols

    # ---- Private Methods ----

    def _update_properties(self):
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.row_vectors = self.matrix
        self.column_vectors = list(zip(*self.matrix))

    # ---- Public Methods ----

    def add_matrix(self, other: Matrix, coeff=1) -> None:
        if not self:
            raise TypeError("Matrices need to be the same dimensions")

        for row in range(self.rows):
            for col in range(self.cols):
                self.matrix[row][col] += other.matrix[row][col] * coeff

        self._update_properties()

    def mult_matrix(self, other: Matrix) -> None:
        in_matrix: M = []
        if self.rows != other.cols:
            raise ValueError("Matrices must have equal inside dimensions")

        for row in range(self.rows):
            in_matrix.append([])
            for col in range(other.cols):
                val = 0

                for n in range(self.cols):
                    c = self.row_vectors[row][n] * other.column_vectors[col][n]
                    val += c

                in_matrix[row].append(val)

        self.matrix = in_matrix
        self._update_properties()

    @property
    def trace(self) -> float:
        if not self.square:
            raise ValueError("Matrix must be square to have a trace")

        trace: float = 0
        for n in range(self.cols):
            trace += self.matrix[n][n]

        return trace

    def transpose(self) -> None:
        in_matrix: M = []

        for col in range(self.cols):
            in_matrix.append([])
            for row in range(self.rows):
                in_matrix[col].append(self.matrix[row][col])

        self.matrix = in_matrix
        self._update_properties()

    def augment_matrix(self, other: Matrix) -> None:
        if self.rows != other.rows:
            raise ValueError("Cannot augment matrices with mismatching number of rows")

        in_matrix: M = []

        for self_rows in range(self.rows):
            in_matrix.append([])
            for self_cols in range(self.cols):
                in_matrix[self_rows].append(self.matrix[self_rows][self_cols])

        for other_rows in range(other.rows):
            for other_cols in range(other.cols):
                in_matrix[other_rows].append(other.matrix[other_rows][other_cols])

        self.matrix = in_matrix
        self._update_properties()

    def gaussian(self):
        self.matrix = elimination(self.matrix, False)
        self._update_properties()

    def reverse_multiplication(self, other: Matrix) -> None:
        """

        .. math::
            AX=B
        """

        in_matrix: M = []

        cols_self = self.cols - 1
        self.augment_matrix(other)
        self.gaussian()
        self._update_properties()
        for row in range(self.rows):
            in_matrix.append([])
            for column in range(self.cols):
                if column > cols_self:
                    in_matrix[row].append(self.matrix[row][column])

        self.matrix = in_matrix
        self._update_properties()

    def inverse(self) -> None:
        if self.rows != self.cols:
            raise ValueError("Matrix must be square to take inverse")

        og_matrix = Matrix(self.matrix)
        identity = self.create_identity(self.rows)
        self.reverse_multiplication(identity)
        inverse = self.matrix

        self.mult_matrix(og_matrix)

        if self.matrix != identity.matrix:
            raise ValueError("Matrix does not have an inverse")

        else:
            self.matrix = inverse
            self._update_properties()

import class_matrix as c

matrix1 = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = c.Matrix([[4, 2, 0], [6, 7, 9], [0, 0, 7]])


def test_add_matricies():
    testmatrix1 = matrix1
    testmatrix2 = matrix2
    testmatrix1.add_matrix(testmatrix2)
    assert testmatrix1.matrix == [[5, 4, 3], [10, 12, 15], [7, 8, 16]]
    testmatrix1.add_matrix(testmatrix2, -1)
    assert testmatrix1.matrix == matrix1.matrix


def test_():
    testmatrix1 = matrix1
    testmatrix2 = matrix2

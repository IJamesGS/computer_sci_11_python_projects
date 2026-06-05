import pytest

import class_matrix as c

matrix_33A = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix_33B = c.Matrix([[4, 2, 0], [6, 2, 1], [6, 7, 9]])

matrix_23 = c.Matrix([[1, 3, 5], [7, 9, 8]])

matrix_32 = c.Matrix([[6, 7], [6, 9], [4, 2]])


def test_add_matricies():
    testmatrix1 = matrix_33A
    testmatrix2 = matrix_33B
    testmatrix3 = matrix_23
    testmatrix1.add_matrix(testmatrix2)
    assert testmatrix1.matrix == [[5, 4, 3], [10, 7, 7], [13, 15, 18]]

    with pytest.raises(ValueError):
        testmatrix1.add_matrix(testmatrix3)


def test_mult_matrix():
    testmatrix4 = matrix_33A
    testmatrix5 = matrix_33B
    testmatrix4.mult_matrix(testmatrix5)
    assert testmatrix4.matrix == [
        [34, 27, 29],
        [82, 60, 59],
        [130, 93, 89],
    ]

    testmatrix6 = matrix_23
    testmatrix7 = matrix_32
    testmatrix6.mult_matrix(testmatrix7)
    assert testmatrix6.matrix == [[44, 44], [128, 146]]

    testmatrix1 = matrix_32
    testmatrix2 = matrix_23
    testmatrix1.mult_matrix(testmatrix2)
    assert testmatrix1.matrix == [
        [55, 81, 86],
        [69, 99, 102],
        [18, 30, 36],
    ]

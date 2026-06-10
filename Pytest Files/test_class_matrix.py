import pytest

import class_matrix as c

matrix_33A = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix_33B = c.Matrix([[4, 2, 0], [6, 2, 1], [6, 7, 9]])

matrix_23 = c.Matrix([[1, 3, 5], [7, 9, 8]])

matrix_32 = c.Matrix([[6, 7], [6, 9], [4, 2]])


def test_add_matricies():
    testmatrix1 = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    testmatrix2 = c.Matrix([[4, 2, 0], [6, 2, 1], [6, 7, 9]])
    testmatrix3 = matrix_23
    testmatrix1.add_matrix(testmatrix2)
    assert testmatrix1.matrix == [[5, 4, 3], [10, 7, 7], [13, 15, 18]]

    with pytest.raises(ValueError):
        testmatrix1.add_matrix(testmatrix3)


def test_mult_matrix():
    testmatrix4 = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    testmatrix5 = c.Matrix([[4, 2, 0], [6, 2, 1], [6, 7, 9]])
    testmatrix4.mult_matrix(testmatrix5)
    assert testmatrix4.matrix == [
        [34, 27, 29],
        [82, 60, 59],
        [130, 93, 89],
    ]

    testmatrix6 = c.Matrix([[1, 3, 5], [7, 9, 8]])
    testmatrix7 = c.Matrix([[6, 7], [6, 9], [4, 2]])
    testmatrix6.mult_matrix(testmatrix7)
    assert testmatrix6.matrix == [[44, 44], [128, 146]]

    testmatrix1 = c.Matrix([[6, 7], [6, 9], [4, 2]])
    testmatrix2 = c.Matrix([[1, 3, 5], [7, 9, 8]])
    testmatrix1.mult_matrix(testmatrix2)
    assert testmatrix1.matrix == [
        [55, 81, 86],
        [69, 99, 102],
        [18, 30, 36],
    ]


def test_trace():
    testmatrix1 = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert testmatrix1.trace == 15


def test_transpose():
    testmatrix1 = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    testmatrix1.transpose()
    assert testmatrix1.matrix == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


def test_augment_matrix():
    testmatrix1 = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    testmatrix2 = c.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    testmatrix2.transpose()
    testmatrix1.augment_matrix(testmatrix2)
    assert testmatrix1.matrix == [
        [1, 2, 3, 1, 4, 7],
        [4, 5, 6, 2, 5, 8],
        [7, 8, 9, 3, 6, 9],
    ]

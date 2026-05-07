import matrix_arithmetic as ma

matrix_33A = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

matrix_33B = [[4, 2, 0],
              [6, 2, 1],
              [6, 7, 9]]

matrix_23 = [[1, 3, 5],
             [7, 9, 8]]

matrix_32 = [[6, 7],
             [6, 9],
             [4, 2]]

def test_get_vectors():
    assert ma.get_vectors(matrix_33A, 'row') == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert ma.get_vectors(matrix_33B, 'column') == [[4, 6, 6],[2, 2, 7],[0, 1, 9]]

def test_get_dimensions():
    assert ma.get_dimensions(matrix_33A) == (3, 3)
    assert ma.get_dimensions(matrix_23) == (2, 3)
    assert ma.get_dimensions(matrix_32) == (3, 2)

def test_same_dimensions():
    assert ma.same_dimensions(matrix_33A, matrix_33B) == True
    assert ma.same_dimensions(matrix_33B, matrix_33A) == True
    assert ma.same_dimensions(matrix_33B, matrix_23) == False
    assert ma.same_dimensions(matrix_33A, matrix_23) == False

def test_add_matricies():
    assert ma.add_matricies(matrix_33A, matrix_33B) == [[5, 4, 3],[10, 7, 7],[13, 15, 18]]
    assert ma.add_matricies(matrix_23, matrix_32) == 'error'

def test_multiply_matricies():
    assert ma.multiply_matricies(matrix_33A, matrix_33B) == [[34, 27, 29],[82, 60, 59],[130, 93, 89]]
    assert ma.multiply_matricies(matrix_23, matrix_32) == [[44, 44], [128, 146]]
    assert ma.multiply_matricies(matrix_32, matrix_23) == [[55, 81, 86],[69, 99, 102],[18, 30, 36]]
    assert ma.multiply_matricies(matrix_33A, [[0,0,0],[0,0,0],[0,0,0]]) == [[0,0,0],[0,0,0],[0,0,0]]
    
def test_augment_matricies():
    assert ma.augment_matricies(matrix_33A, matrix_33B) == [[1, 2, 3, 4, 2, 0],[4, 5, 6, 6, 2, 1],[7, 8, 9, 6, 7, 9]]
    assert ma.augment_matricies(matrix_23, matrix_32) == 'error'
    
def test_solve_AX_to_B():
    assert ma.solve_AX_to_B([[1,0,2],[0,-1,-2],[2,-1,0]], [[-1,2],[2,-6],[2,-4]]) == [[1,0],[0,4],[-1,1]]
    
def test_matrix_transpose():
    assert ma.matrix_transpose(matrix_33A) == [[1,4,7],[2,5,8],[3,6,9]]
    assert ma.matrix_transpose(matrix_23) == [[1,7],[3,9],[5,8]]

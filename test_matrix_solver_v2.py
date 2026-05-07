from matrix_solver_v2 import swap_rows, multiply_row, add_rows, solve, create_matrix_list
from copied_gaussian_algorithm import benchmark
from math import isclose

# copy and paste
test_matrix = [[2, 1, -1, 4 ],
               [1, -1, 2, 12],
               [2, 2, -1, 9 ]]

answer_matrix = [[1, 0, 0, 3],
                 [0, 1, 0, 5],
                 [0, 0, 1, 7]] # #of sol'ns = 1

zero_matrix = [[0, 0],
               [0, 0]]

small_matrix = [[1, 15],
                [3, 45]]

single_row_matrix = [[13, 26]]

def test_solve_standard():
    assert solve([[2,3,7],[-4,6,-2]]) == (([[1.0, 0.0, 2.0], [0.0, 1.0, 1.0]]), 1)
    assert solve([[2,3,7],[ 4,6,-2]])[1] == 0
    assert solve([[2,3,7],[4,6,14]])[1] == 2
    assert solve([[2,3,12],[-4,6,0]]) == (([[1.0, 0.0, 3.0], [0.0, 1.0, 2.0]]), 1)
    assert solve(test_matrix) == ((answer_matrix), 1)

    
def test_solve_small():
    assert solve(small_matrix) == ([[1, 15],[0, 0]], 1)
    
def test_solve_small_zero():
    assert solve(zero_matrix) == ([[0,0],[0,0]], 0)

def test_solve_single_row():
    assert solve(single_row_matrix) == ([[1, 2]], 1)
    
def test_solve_already_solved():
    answer_matrix = [[1, 0, 0, 3],[0, 1, 0, 5],[0, 0, 1, 7]]
    assert solve(answer_matrix) == ([[1, 0, 0, 3],[0, 1, 0, 5],[0, 0, 1, 7]], 1)
    answer_matrix = [[1, 0, 0, 3],[0, 1, 0, 5],[0, 0, 1, 7]]
  
def test_swap_rows_standard():
    test_matrix = [[2, 1, -1, 4 ],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert swap_rows(test_matrix, 0, 1) == [[1, -1, 2, 12],[2, 1, -1, 4 ],[2, 2, -1, 9]]
    
    test_matrix = [[2, 1, -1, 4 ],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert swap_rows(test_matrix, 1, 2) == [[2, 1, -1, 4],[2, 2, -1, 9],[1, -1, 2, 12]]
    
def test_swap_rows_same():
    test_matrix = [[2, 1, -1, 4 ],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert swap_rows(test_matrix, 0, 0) == test_matrix
    
    test_matrix = [[2, 1, -1, 4 ],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert swap_rows(test_matrix, 1, 1) == test_matrix
    
    test_matrix = [[2, 1, -1, 4 ],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert swap_rows(test_matrix, 2, 2) == test_matrix

def test_multiply_row_standard():
    test_matrix = [[2, 1, -1, 4],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert multiply_row(test_matrix, 0, 2) == [[4, 2, -2, 8],[1, -1, 2, 12],[2, 2, -1, 9]]
    
    test_matrix = [[2, 1, -1, 4],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert multiply_row(test_matrix, 2, -10) == [[2, 1, -1, 4 ],[1, -1, 2, 12],[-20, -20, 10, -90]]

def test_add_rows_standard():
    test_matrix = [[2, 1, -1, 4],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert add_rows(test_matrix, 0, 1, 1) == [[3, 0, 1, 16],[1, -1, 2, 12],[2, 2, -1, 9]]
    
    test_matrix = [[2, 1, -1, 4],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert add_rows(test_matrix, 2, 1, -5) == [[2, 1, -1, 4],[1, -1, 2, 12],[-3, 7, -11, -51]]
    
def test_benchmark_standard():
    test_matrix = [[2, 1, -1, 4],[1, -1, 2, 12],[2, 2, -1, 9]]
    assert solve(test_matrix) == benchmark(test_matrix)
    
def test_forthomsas():
    #good assert solve([[34, 5555, 1],[1, 2, 67],[333,33,3]]) == ([[1,0,67.82996172772006],[0,1,-0.4149808638600328],[0,0,1]], 0)
    #good assert solve([[1],[2],[3]]) == ([[0],[0],[0]], 0)
    assert solve([6, 12]) == ([1, 2], 1)
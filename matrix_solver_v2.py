'''
Program with functions to:
-print matricies neatly in a shell
-easily input matricies via shell to store as variables
-do basic matrix operations (add rows, multiply rows, swap rows)
-simplify a matrix via a gaussian elimination algorithm that takes in any size matrix and outputs a matrix with the
same dimensions in reduced-row echelon form
-output the nature of the solution to a matrix
'''
#define types
M: type = list[list[float]]

def print_matrix(matrix):
    """Display matrix in shell"""
    for _ in matrix:
        for value in row:
            print(str(value), end=' ')
        print()


def input_matrix():
    """Input matrix via shell"""
    in_matrix: M = list()
    columns: int = int(input('# of columns in matrix: \n'))
    rows: int = int(input('# of rows in matrix: \n'))
    
    # check if the inputed dimensions are a valid matrix
    if rows < 1 or columns < 2:
        raise TypeError("Not a valid matrix")
    
    # get values for each entry in matrix
    for row in range(rows):
        in_matrix.append([])
        for column in range(columns):
            value: int = int(input("Enter value for row " + str(row) + " column " + str(column) + ': \n'))
            in_matrix[row].append(value)
            
    return in_matrix

def swap_rows(matrix, row1, row2): 
    """Swap two rows with one another"""
    in_matrix = matrix
    r1 = in_matrix[row1].copy()
    r2 = in_matrix[row2].copy()
    r1, r2 = r2, r1
    in_matrix.insert(row1, r1)
    in_matrix.pop(row1 + 1)
    in_matrix.insert(row2, r2)
    in_matrix.pop(row2 + 1)
    return in_matrix

def multiply_row(matrix, row, factor):
    """Multiply matrix row by a factor"""
    in_matrix = matrix
    for n in range(len(in_matrix[row])):
        in_matrix[row][n] = in_matrix[row][n] * factor
    
    return in_matrix

def add_rows(matrix, row1, row2, coeff): 
    """Add two rows in a matrix"""
    in_matrix = matrix
    for n in range(len(in_matrix[row1])):
        applied_row2 = in_matrix[row2][n] * coeff
        in_matrix[row1][n] = in_matrix[row1][n] + applied_row2
    
    return in_matrix


def elimination(matrix, pvt=0):
    """Gaussian Elimination"""
    # to break nested loops
    good = True
    in_matrix = matrix
    # list of pivot positions aka where leading entries are in the matrix, and later the positions of leading 1s
    # each pivot is a list such that [x, y], with [0, 0] being the first row and first column in a matrix
    pivots: list[list[int]] = []
    # correcting the algorithm based on the dimensions of the matrix
    if len(in_matrix) == len(in_matrix[0]) - 1:
        correction = -1
        
    elif len(in_matrix) > len(in_matrix[0]) - 1:
        correction = len(in_matrix) - len(in_matrix[0])
    
    elif len(in_matrix) < len(in_matrix[0]) - 1:
        correction = len(in_matrix) - len(in_matrix[0])
    
    # step 1 - find first pivot position and place it in first row
    for column in range(len(in_matrix[0])): 
        for row in range(len(in_matrix)):
            if in_matrix[row][column] != 0 and good:
                in_matrix = swap_rows(in_matrix, 0, row)
                pivot = [column, 0]
                pivots.append(pivot)
                good = False # essentially breaks the nested loop early or else bad things happen
    
    # if there are no valid pivot positions, must be a zero matrix w/ no solutions
    if len(pivots) == 0:
        if pvt == 0:
            return in_matrix, 0
        else:
            return in_matrix
    
    good = True
    
    # step 2 - make all entries under pivot position equal to zero through addition
    for row in range(len(in_matrix[0]) + correction): 
        if in_matrix[row][pivot[0]] != 0 and row > pivot[1]:
            in_matrix = add_rows(in_matrix, row, pivot[1], -(in_matrix[row][pivot[0]]/ in_matrix[pivot[1]][pivot[0]]))
    
    # step 3 - repeat steps 1 and 2 using the position of first pivot to find the remaining pivots
    for _ in range(len(in_matrix) + 1):
        # step 3.1 - find pivot and correctly place
        
        good = True
        for row in range(len(in_matrix)):    
            for column in range(len(in_matrix[0]) - 1):   
                if row > pivot[1] and column > pivot[0] and row < len(in_matrix) and good:    
                    if in_matrix[column][row] != 0:
                        in_matrix = swap_rows(in_matrix, row, pivot[1] + 1)
                        good = False
                        previous_pivot = pivot
                        pivot = [column, previous_pivot[1] + 1]
                        pivots.append(pivot)
                        
        
        
        
        
        # step 3.2 - make all entries under pivot position equal to zero through addition
        for row in range(len(in_matrix[0]) + correction): 
            if in_matrix[row][pivot[0]] != 0 and row > pivot[1]:
                in_matrix = add_rows(in_matrix, row, pivot[1], -(in_matrix[row][pivot[0]] / in_matrix[pivot[1]][pivot[0]]))
        
        if len(pivots) == len(in_matrix[0]):
            break

    # step 4 - turn each leading entry to 1
    for n in range(len(pivots)):
        if in_matrix[pivots[n][0]][pivots[n][1]] != 1:
            in_matrix = multiply_row(matrix, pivots[n][1], (1 / matrix[pivots[n][0]][pivots[n][1]]))
            
    # step 5 - create zeros in entries above pivots
    for n in range(len(pivots)):
        for row in range(len(in_matrix)):
            if in_matrix[row][pivots[n][0]] != 0 and row < pivots[n][1]:
                in_matrix = add_rows(in_matrix, row, pivots[n][0], -(in_matrix[row][pivots[n][0]]))      
        
    # create leading entry = 1 if the only none-zero value in a row is in the last column, then make it the last row
    # unneccesary step for asthetics, can be removed if desired
    zero_row_minus1 = [0]*(len(in_matrix[0]) - 1)
    for row in range(len(in_matrix)):
        if in_matrix[row][0:len(in_matrix[0]) - 1] == zero_row_minus1 and in_matrix[row][len(in_matrix[0]) - 1] != 0:
            in_matrix = multiply_row(in_matrix, row, (1 / in_matrix[row][len(in_matrix[0]) - 1]))
            new_row = in_matrix[row]
            in_matrix.pop(row)
            in_matrix.append(new_row)
            
    # go through all the values & clean them up (remove the floating-point errors)
    for row in range(len(in_matrix)):
        for n in range(len(in_matrix[0])):
            in_matrix[row][n] = round(in_matrix[row][n], 13)
    
    # all done (:
    if pvt == 0:
        return in_matrix, pivots
    else:
        return in_matrix

# fuction to determine the number of solutions in a matrix
def find_soln(matrix, pivots):
    in_matrix = matrix
    
    zero_row_minus1 = [0]*(len(in_matrix[0]) - 1)
    
    #if there are no pivots, must be a zero matrix and therefor no solutions
    if pivots == 0:
        return 0
    
    # check if the system is inconsistant first
    for row in range(len(in_matrix)):
        
        # if inconsistant, 0 solutions
        if in_matrix[row][0:len(in_matrix[0]) - 1] == zero_row_minus1 and in_matrix[row][len(in_matrix[0]) - 1] != 0:
            solution = 0
        
        # if not inconsistant, must be consistant (duh!)
        else:
            # check if each variable has a leading 1
            if len(pivots) == len(in_matrix[0]) - 1:
                solution = 1
            
            # if not 1 solution and consistant, MUST be infinite solutions
            else:
                solution = 2
            
    return solution

def execute():
    go = True
    while go:
        old_matrix = input_matrix()

        if old_matrix != "error":
            print("\nold matrix: \n")
            print_matrix(old_matrix)
            
            new_matrix, matrix_pivots = elimination(old_matrix)
            print("\nnew matrix: \n")
            print_matrix(new_matrix)
            
            solutions = find_soln(new_matrix, matrix_pivots)
            
            if solutions == 2:
                solutions = "infinite"
                
            print('\n# of sol\'n:', solutions)

        else:
            print('error, need at least a 2x2 matrix')
            
        cont = input("\ninput any key & hit enter to stop\n")
        if cont != None:
            go = False

# function for unit testing via pytest
def solve(matrix):
    new_matrix, pivots = elimination(matrix)
    solutions = find_soln(new_matrix, pivots)
    return new_matrix, solutions

# function to create a list of matricies with every combination of the following values:
def create_matrix_list(min_value, max_value, max_columns, max_rows):
    matrix_list: list[list[list[float]]] = []
    matrix: list[list[float]] = []
    if max_value < min_value:
        print('error: max_value < min_value')
        return
    
    if max_columns < 2 or max_rows < 2:
        print('error: max_columns or max_rows < 2')
        return
    
    for a in range(2, max_rows + 1):
        for b in range(2, max_columns + 1):
                matrix = list()
                for n in range(0, a):
                    matrix.append([])
                    for _ in range(0, b):
                        matrix[n].append(0)
                
                for row in range(len(matrix)):
                    for column in range(len(matrix[0])):
                        for c in range(min_value, max_value + 1):
                            if c != 0:
                                matrix[row][column] = c
                                matrix_list.append(matrix)
                            

    return matrix_list


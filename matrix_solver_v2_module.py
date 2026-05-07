'''
Program with functions to:
-print matricies neatly in a shell
-easily input matricies via shell to store as variables
-do basic matrix operations (add rows, multiply rows, swap rows)
-simplify a matrix via a gaussian elimination algorithm that takes in any size matrix and outputs a matrix with the
same dimensions in reduced-row echelon form
-output the nature of the solution to a matrix
'''


# function to help display the matrixices better in the shell
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(str(value), end=' ')
        print()
    
# fuction to input a matrix through the shell and store as a variable
def input_matrix():
    matrix = []
    columns = int(input('# of columns in matrix: \n'))
    rows = int(input('# of rows in matrix: \n'))
    
    # check if the inputed dimensions are a valid matrix
    if rows < 2 or columns < 2:
        return "error"
    
    # get values for each entry in matrix
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            value = int(input("Enter value for row " + str(row) + " column " + str(column) + ': \n'))
            matrix[row].append(value)
            
    return matrix

# swap row1 and row2 with one another in a matrix
def swap_rows(matrix, row1, row2): 
    r1 = matrix[row1].copy()
    r1copy = r1
    r2 = matrix[row2].copy()
    r2copy = r2
    r1 = r2copy
    r2 = r1copy
    matrix.insert(row1, r1)
    matrix.pop(row1 + 1)
    matrix.insert(row2, r2)
    matrix.pop(row2 + 1)
    return matrix

# multiply rows in a matrix such that row1 * factor -> row1
def multiply_row(matrix, row, factor):
    for n in range(len(matrix[row])):
        matrix[row][n] = matrix[row][n] * factor
    
    return matrix

# add rows in a matrix such that row1 + coeff*row2 -> row1
def add_rows(matrix, row1, row2, coeff): 
    for n in range(len(matrix[row1])):
        applied_row2 = matrix[row2][n] * coeff
        matrix[row1][n] = matrix[row1][n] + applied_row2
    
    return matrix

# gaussian elimination algorithm
def elimination(matrix):
    # to break nested loops
    good = True
    
    # list of pivot positions aka where leading entries are in the matrix, and later the positions of leading 1s
    # each pivot is a list such that [x, y], with [0, 0] being the first row and first column in a matrix
    pivots = []
    
    # correcting the algorithm based on the dimensions of the matrix
    if len(matrix) == len(matrix[0]) - 1:
        correction = -1
        
    elif len(matrix) > len(matrix[0]) - 1:
        correction = len(matrix) - len(matrix[0])
    
    elif len(matrix) < len(matrix[0]) - 1:
        correction = len(matrix) - len(matrix[0])
    
    # step 1 - find first pivot position and place it in first row
    for column in range(len(matrix[0])): 
        for row in range(len(matrix)):
            if matrix[row][column] != 0 and good:
                swap_rows(matrix, 0, row)
                pivot = [column, 0]
                pivots.append(pivot)
                good = False # essentially breaks the nested loop early or else bad things happen
                
    good = True
    
    # step 2 - make all entries under pivot position equal to zero through addition
    for row in range(len(matrix[0]) + correction): 
        if matrix[row][pivot[0]] != 0 and row > pivot[1]:
            add_rows(matrix, row, pivot[1], -(matrix[row][pivot[0]]/matrix[pivot[1]][pivot[0]]))
    
    # step 3 - repeat steps 1 and 2 using the position of first pivot to find the remaining pivots
    for m in range(len(matrix) + 1):
        
        # step 3.1 - find pivot and correctly place
        for row in range(len(matrix)):    
            for column in range(len(matrix[0]) - 1):   
                if row > pivot[1] and column > pivot[0] and row < len(matrix):
                    if matrix[column][row] != 0 and good and column > pivot[0]:
                        swap_rows(matrix, row, pivot[1] + 1)
                        good = False
                        previous_pivot = pivot
                        pivot = [column, previous_pivot[1] + 1]
                        pivots.append(pivot)
                        
        good = True
        
        # step 3.2 - make all entries under pivot position equal to zero through addition
        for row in range(len(matrix[0]) + correction): 
            if matrix[row][pivot[0]] != 0 and row > pivot[1]:
                add_rows(matrix, row, pivot[1], -(matrix[row][pivot[0]]/matrix[pivot[1]][pivot[0]]))
        
        if len(pivots) == len(matrix[0]):
            break
        
    # step 4 - turn each leading entry to 1
    for n in range(len(pivots)):
        if matrix[pivots[n][0]][pivots[n][1]] != 1:
            multiply_row(matrix, pivots[n][1], (1 / matrix[pivots[n][0]][pivots[n][1]]))
            
    # step 5 - create zeros in entries above pivots
    for n in range(len(pivots)):
        for row in range(len(matrix)):
            if matrix[row][pivots[n][0]] != 0 and row < pivots[n][1]:
                add_rows(matrix, row, pivots[n][0], -(matrix[row][pivots[n][0]]))      
        
    # create leading entry = 1 if the only none-zero value in a row is in the last column, then make it the last row
    # unneccesary step for asthetics, can be removed if desired
    zero_row_minus1 = [0]*(len(matrix[0]) - 1)
    for row in range(len(matrix)):
        if matrix[row][0:len(matrix[0]) - 1] == zero_row_minus1 and matrix[row][len(matrix[0]) - 1] != 0:
            multiply_row(matrix, row, (1 / matrix[row][len(matrix[0]) - 1]))
            new_row = matrix[row]
            matrix.pop(row)
            matrix.append(new_row)
            
    # all done (:
    return matrix, pivots

# fuction to determine the number of solutions in a matrix
def find_soln(matrix, pivots):
    zero_row = [0]*len(matrix[0])
    zero_row_minus1 = [0]*(len(matrix[0]) - 1)
    consistant = False
    
    # check if the system is inconsistant first
    for row in range(len(matrix)):
        # if inconsistant, 0 solutions
        if matrix[row][0:len(matrix[0]) - 1] == zero_row_minus1 and matrix[row][len(matrix[0]) - 1] != 0:
            solution = 0
        
        # if not inconsistant, must be consistant (duh!)
        else:
            # check if each variable has a leading 1
            if len(pivots) == len(matrix[0]) - 1:
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

def py_function(matrix):
    new_matrix, pivots = elimination(matrix)
    solutions = find_soln(new_matrix, pivots)
    return new_matrix, solutions

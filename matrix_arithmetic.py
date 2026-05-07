from matrix_solver_v2 import print_matrix, elimination

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

# returns # of rows, cols of matrix
def get_dimensions(matrix):
    try:
        rows = len(matrix)
        cols = len(matrix[0])
        return rows, cols
    
    except Exception as e:
        return "error"
        print(f"Something went wrong: {e}")

# takes in two matricies, and checks if they have the same number of columns and rows
def same_dimensions(A, B):
    try:
        rows_A, cols_A = get_dimensions(A)
        rows_B, cols_B = get_dimensions(B)
        
        if rows_A == rows_B and cols_A == cols_B:
            return True
        
        else:
            return False
    
    except Exception as e:
        return "error"
        print(f"Something went wrong: {e}")

# take in matricies A & B, adds them, returns a new matrix C
def add_matricies(A, B, Acoeff=1, Bcoeff=1):
    try:
        C: list[list[float]] = list()
        
        # check if the matricies have the same dimensions
        if same_dimensions(A, B) == False:
            return "error"
        
        rows, cols = get_dimensions(A)
        
        # create new matrix "C"
        for row in range(rows):
            C.append([])
            for col in range(cols):
                C[row].append(0)
        
        # adds all the values of matrix A times a coeffecient to C
        for row in range(rows):
            for col in range(cols):
                C[row][col] = (A[row][col]) * Acoeff
        # same as above, but with matrix B
        for row in range(rows):
            for col in range(cols):
                C[row][col] = C[row][col] + ((B[row][col]) * Bcoeff)
        
        return C
    
    except Exception as e:
        return "error"
        print(f"Something went wrong: {e}")
        
# returns a list of the row and/or column vectors of matrix A
def get_vectors(A, which_vector="both"):
    try:
        row_vectors = list()
        col_vectors = list()
        
        if which_vector == "row":
            for row in range(len(A)):
                row_vectors.append(A[row])
                
            return row_vectors
                
        elif which_vector == "column":
            for col in range(len(A[0])):
                temp_col_vect = list()
                for row in range(len(A)):
                    temp_col_vect.append(A[row][col])
                
                col_vectors.append(temp_col_vect)
        
            return col_vectors
        
        elif which_vector == "both":
            for col in range(len(A[0])):
                temp_col_vect = list()
                for row in range(len(A)):
                    temp_col_vect.append(A[row][col])
                
                col_vectors.append(temp_col_vect)
            
            for row in range(len(A)):
                row_vectors.append(A[row])
                
            return col_vectors, row_vectors
    
    except Exception as e:
        return f"error: {e}"
        print(f"Something went wrong: {e}")
    
# returns the product of matrix A & B in a matrix C
def multiply_matricies(A, B):
    try:
        A_vectors = get_vectors(A, 'row')
        B_vectors = get_vectors(B, 'column')
        C: list[list[float]] = list()
        
        if len(A_vectors[0]) != len(B_vectors[0]):
            return 'error'
        
        for row in range(len(A_vectors)):
            C.append(list())
            for col in range(len(B_vectors)):
                #set up "val" for the final assigment of variable
                val = 0
                #loop through the vectors
                for n in range(len(A_vectors[0])):
                    c = 0
                    #multiply corrosponding values between the vectors as c
                    c = (A_vectors[row][n] * B_vectors[col][n])
                    #add c to the value, c is then reset on the loop
                    val += c
                #val becomes the entry in the C matrix
                C[row].append(val)
        
        return C
    
    except Exception as e:
        return "other_error"
        print(f"Something went wrong: {e}")

# creates the augmented matrix [A|B]
def augment_matricies(A, B):
    try:
        C: list[list[float]] = list()
        for row1 in range(len(A)):
            C.append([])
            for column1 in range(len(A[0])):
                C[row1].append(A[row1][column1])
        for row in range(len(B)):
            for column in range(len(B[0])):
                C[row].append(B[row][column])
                
        return C
    
    except Exception as e:
        return "error"
        print(f"Something went wrong: {e}")

# returns the X matrix which solves the equation AX = B
def solve_AX_to_B(A, B):
    try:
        X: list[list[float]] = list()
            
        cols_A = len(A[0]) - 1
        AB = augment_matricies(A, B)
        #runs the augmented matrix througn gaussian elimination
        new_AB = elimination(AB, "nopivots")
        #new_AB is now in the form [I|X]
        #"unaugments" the matrix to aquire X
        for row in range(len(new_AB)):
            X.append([])
            for column in range(len(new_AB[0])):
                if column > cols_A:
                    X[row].append(new_AB[row][column])
            
        return X
    
    except Exception as e:
        return f"Something went wrong: {e}"
        print(f"Something went wrong: {e}")

# returns the transposed matrix A as B
def matrix_transpose(A):
    try:
        B: list[list[float]] = list()

        for column in range(len(A[0])):
            B.append([])
            for row in range(len(A)):
                B[column].append(A[row][column])
                
        return B
    
    except Exception as e:
        return "error"
        print(f"Something went wrong: {e}")

# returns a new nxn identity matrix A
def create_identity(n):
    if n < 1:
        return 'error'
    
    A: list[list[float]] = list()
    
    for row in range(n):
        A.append(list())
        for column in range(n):
            if row == column:
                A[row].append(1)
            else:
                A[row].append(0)
                
    return A

# returns matrix X which solves AX = I
def matrix_inverse(A):
    
    #check square
    Ar, Ac = get_dimensions(A)
    if Ar != Ac:
        return 'error'
    
    identity = create_identity(len(A))
    
    X = solve_AX_to_B(A, identity)
    
    #check if X is actually the inverse of A
    check = multiply_matricies(A, X)
    
    if check == identity:
        return X
    
    if check != identity:
        return 'matrix uninvertible'

# returns the trace of a square matrix A
def trace(A):
    t: float = 0
    
    #check square
    Ar, Ac = get_dimensions(A)
    if Ar != Ac:
        return 'error'
    
    for row in range(len(A)):
        for column in range(len(A[0])):
            if row == column:
                t += A[row][column]
                
    return t

# returns the determinate of a square matrix A that is less than 2 in dimensions
def determinate_2_and_small(A):
    d: float = 0
    
    #check square
    Ar, Ac = get_dimensions(A)
    if Ar != Ac:
        return 'error'
    
    An = Ar
    if An == 1:
        d = A[0][0]
    
    elif An == 2:
        d = ((A[0][0]) *  (A[1][1])) - ((A[0][1]) * (A[1][0]))
        
    else:
        return 'too big!'
    
    return d
    
#returns the product of Ab = c
def mult_vector(A, b):
    c: list[float] = list()
    
    if len(A[0]) != len(b):
        return "error"
    
    for row in range(len(A)):
        val = 0
        for column in range(len(A[0])):
            x = A[row][column] * b[column]
            val += x
            
        c.append(val)
    
    
    return c
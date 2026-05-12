from matrix_solver_v2 import elimination

Matrix: type = list[list[float]]
Vector: type = list[float]

def get_dimensions(matrix: Matrix):
    """Get the number of rows and columns in a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    return rows, cols


def same_dimensions(A: Matrix, B:Matrix) -> bool:
    """Check if two matrices have the same number of columns and rows."""
    rows_A, cols_A = get_dimensions(A)
    rows_B, cols_B = get_dimensions(B)

    return rows_A == rows_B and cols_A == cols_B


def add_matricies(A: Matrix, B: Matrix, Acoeff=1, Bcoeff=1) -> Matrix:
    """Add two matrices together."""
    output: Matrix = []

    # check if the matrices have the same dimensions
    if same_dimensions(A, B) == False:
        raise ValueError("Matrices have mismatched dimensions.")

    rows, cols = get_dimensions(A)

    # create new matrix "C"
    for row in range(rows):
        output.append([])
        for _ in range(cols):
            output[row].append(0)

    # adds all the values of matrix A times a coefficient to C
    for row in range(rows):
        for col in range(cols):
            output[row][col] = (A[row][col]) * Acoeff
    # same as above, but with matrix B
    for row in range(rows):
        for col in range(cols):
            output[row][col] = output[row][col] + ((B[row][col]) * Bcoeff)

    return output


def get_row_vectors(
    in_matrix: Matrix
) -> list[Vector]:
    """Get a list of the row and/or column vectors of the matrix."""
    output = []

    for row in range(len(in_matrix)):
        output.append(in_matrix[row])

    return output


def get_column_vectors(
    in_matrix: Matrix
) -> list[Vector]:
    output = []
    
    for col in range(len(in_matrix[0])):
        temp_col_vect = []
        for row in range(len(in_matrix)):
            temp_col_vect.append(in_matrix[row][col])

        output.append(temp_col_vect)

    return output


def multiply_matricies(A: Matrix, B: Matrix) -> Matrix:
    """Get the product of A * B as a matrix."""
    A_vectors = get_row_vectors(A)
    B_vectors = get_column_vectors(B)
    output: Matrix = []

    if len(A_vectors[0]) != len(B_vectors[0]):
        raise ValueError("Matrices have mismatched dimensions.")

    for row in range(len(A_vectors)):
        output.append([])
        for col in range(len(B_vectors)):
            # set up "val" for the final assignment of variable
            val = 0
            # loop through the vectors
            for n in range(len(A_vectors[0])):
                # multiply corresponding values between the vectors as c
                c = A_vectors[row][n] * B_vectors[col][n]
                # add c to the value, c is then reset on the loop
                val += c
            # val becomes the entry in the C matrix
            output[row].append(val)

    return output


def augment_matricies(A: Matrix, B: Matrix) -> Matrix:
    """Create the augmented matrix [A|B]."""
    output: Matrix = []

    for row1 in range(len(A)):
        output.append([])
        for column1 in range(len(A[0])):
            output[row1].append(A[row1][column1])

    for row in range(len(B)):
        for column in range(len(B[0])):
            output[row].append(B[row][column])

    return output


def solve_XA_to_B(A: Matrix, B :Matrix) -> Matrix:
    """Get the X matrix which solves the equation X*A = B."""
    X: Matrix = []

    cols_A = len(A[0]) - 1
    AB = augment_matricies(A, B)
    # runs the augmented matrix through Gaussian Elimination
    new_AB = elimination(AB, "nopivots")
    # new_AB is now in the form [I|X]
    # "unaugments" the matrix to acquire X
    for row in range(len(new_AB)):
        X.append([])
        for column in range(len(new_AB[0])):
            if column > cols_A:
                X[row].append(new_AB[row][column])

    return X


def matrix_transpose(A: Matrix) -> Matrix:
    """Transpose a matrix."""
    output: Matrix = []

    for column in range(len(A[0])):
        output.append([])
        for row in range(len(A)):
            output[column].append(A[row][column])

    return output


def create_identity(size: int) -> Matrix:
    """Creates a new `size`x`size` identity matrix"""
    if size < 1:
        raise ValueError("Matrix must have dimensions greater than 0.")

    output: Matrix = []

    for row in range(size):
        output.append([])
        for column in range(size):
            if row == column:
                output[row].append(1)
            else:
                output[row].append(0)

    return output

def matrix_inverse(in_matrix: Matrix) -> Matrix:
    """Get the inverse of a matrix"""
    # check square
    size_y, size_x = get_dimensions(in_matrix)
    if size_y != size_x:
        raise ValueError("Matrix is not square")

    identity = create_identity(len(in_matrix))

    output: Matrix = solve_XA_to_B(in_matrix, identity)

    # check if X is actually the inverse of A
    check = multiply_matricies(in_matrix, output)

    if check != identity:
        raise ValueError("Matrix cannot be inverted.")

    return output


def trace(in_matrix: Matrix) -> float:
    """Get the trace of a square matrix"""
    t: float = 0

    # check square
    num_rows, num_columns = get_dimensions(in_matrix)
    if num_rows != num_columns:
        raise ValueError("Matrix is not square")

    for row in range(len(in_matrix)):
        for column in range(len(in_matrix[0])):
            if row == column:
                t += in_matrix[row][column]

    return t


# returns the determinate of a square matrix A that is less than 2 in dimensions
def determinate_2_and_small(in_matrix: Matrix) -> float:
    """Get the determinate of a square matrix which is no greater than two entries in either dimension"""
    d: float = 0

    # check square
    num_rows, num_columns = get_dimensions(in_matrix)
    if num_rows != num_columns or num_rows > 2 or num_rows < 1:
        raise ValueError("Matrix must have dimensions 1x1 or 2x2.")

    if num_rows == 1:
        d = in_matrix[0][0]

    elif num_rows == 2:
        d = ((in_matrix[0][0]) * (in_matrix[1][1])) - ((in_matrix[0][1]) * (in_matrix[1][0]))

    return d


# returns the product of Ab = c
def mult_vector(in_matrix: Matrix, b: Vector) -> Vector:
    """Get the product of a matrix and vector multiplication"""
    output: Vector = []

    if len(in_matrix[0]) != len(b):
        raise ValueError("Matrices have mismatched dimensions.")

    for row in range(len(in_matrix)):
        val = 0
        for column in range(len(in_matrix[0])):
            x = in_matrix[row][column] * b[column]
            val += x

        output.append(val)

    return output

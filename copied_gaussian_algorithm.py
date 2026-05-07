def gaussian_elimination(matrix):
    """Performs Gaussian elimination on an augmented matrix in-place."""
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        # Partial Pivoting: Find the row with the maximum absolute value in the current column
        max_row = i
        for k in range(i + 1, rows):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        # Swap rows
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        
        pivot = matrix[i][i]
        # If pivot is near zero after pivoting, system might not have a unique solution.
        # Handle potential division by zero or very small numbers
        if abs(pivot) < 1e-9:
            continue # Move to next column, this column has no free pivot

        # Divide the current row by the pivot to get a leading 1
        for j in range(i, cols):
            matrix[i][j] /= pivot
        
        # Eliminate other rows
        for k in range(rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, cols):
                    matrix[k][j] -= factor * matrix[i][j]
                    
    return matrix

def determine_solution_nature(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    num_vars = cols - 1
    
    # Check for no solution (inconsistency)
    for i in range(rows):
        # Check if the coefficient part of the row is all zeros
        is_zero_row_coeffs = all(abs(matrix[i][j]) < 1e-9 for j in range(num_vars))
        # Check if the constant part is non-zero
        is_nonzero_constant = abs(matrix[i][num_vars]) >= 1e-9
        
        if is_zero_row_coeffs and is_nonzero_constant:
            return 0 #"No solution"
            
    # Check for infinite solutions or unique solution
    rank = 0
    for i in range(rows):
        # Count rank by counting non-zero rows (after checking for inconsistency)
        if not all(abs(matrix[i][j]) < 1e-9 for j in range(cols)):
            rank += 1
            
    if rank == num_vars:
        return 1 #"Unique solution"
    elif rank < num_vars:
        return 2 #"Infinite solutions"
    else:
        # This case generally shouldn't happen with correct Gaussian elimination on well-formed input
        return "Cannot determine"
    
def benchmark(matrix):
    solved_matrix = gaussian_elimination(matrix)
    solutions = determine_solution_nature(solved_matrix)
    return solved_matrix, solutions

# test1, test2 = benchmark([[2, 1, -1, 4 ],[1, -1, 2, 12],[2, 2, -1, 9 ]])
#print(test1)
#print()
#print(test2)
    
    
import math

"""Swaps two rows in the matrix.""" 
def swapRow(matrix, row1, row2):
    tempRow = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = tempRow
    return matrix

"""Divides all elements in a row by a divisor to make the pivot 1.""" 
def scaleRow(matrix, row, divisor):
    for col in range(len(matrix[row])):
        matrix[row][col] = matrix[row][col] / divisor
    return matrix

"""Subtracts (factor * pivotRow) from targetRow to eliminate a column entry."""
def addRow(matrix, rowPivot, rowTarget, factor):
    for col in range(len(matrix[rowPivot])):
        matrix[rowTarget][col] = matrix[rowTarget][col] - (factor * matrix[rowPivot][col])
        
    return matrix

"""Solves a system of linear equations using Gaussian elimination.
Returns: (final_matrix, status_code)
Status Codes: 1 = Unique Solution, 0 = No Solution, 2 = Infinite Solutions """
def doGaussian(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    numVars = numCols - 1 # Last column is the constants (b in Ax=b)

    pivotRow = 0
    for col in range(numVars):
        if pivotRow >= numRows:
            break
            
        # 1. Partial Pivoting: Find the best row to swap with to avoid 0
        maxRow = pivotRow
        for nextRow in range(pivotRow, numRows):
            # vv edited from original algorithm
            if matrix[nextRow][col] != 0:
                maxRow = nextRow
                break
        
        swapRow(matrix, pivotRow, maxRow)
        # 2. Check if the column is effectively zero
        if math.isclose(matrix[pivotRow][col], 0, abs_tol=1e-10):
            matrix[pivotRow][col] = 0
            continue  # Skip this column, it's a free variable candidate
        # 3. Scale the pivot row so the pivot entry is 1
        scaleRow(matrix, pivotRow, matrix[pivotRow][col])
        # 4. Elimination: Zero out the rest of the column (Forward and Backward)
        for r in range(numRows):
            if r != pivotRow:
                factor = matrix[r][col]
                addRow(matrix, pivotRow, r, factor)
        
        pivotRow += 1
    # 5. Determine the number of solutions
    rank = 0
    for r in range(numRows):
        # Check if row is [0, 0, ..., | b] where b != 0
        allZeros = True
        for c in range(numVars):
            if not math.isclose(matrix[r][c], 0, abs_tol=1e-10):
                allZeros = False
                break
        
        if allZeros:
            # If the variable coefficients are all zero but the constant is not
            if not math.isclose(matrix[r][numVars], 0, abs_tol=1e-10):
                return matrix, 0  # No solution (0 = constant)
        else:
            rank += 1

    if rank < numVars:
        return matrix, 2  # Infinite solutions (fewer equations than variables)

    return matrix, 1  # Unique solution
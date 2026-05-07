def matrixAdd(Matrix1, Matrix2):
    resultMatrix: list[list[float]] = list()
    
    num_rows1 = len(Matrix1)
    num_rows2 = len(Matrix2)
    
    try:
        num_cols1 = len(Matrix1[0])
        num_cols2 = len(Matrix2[0])
    except TypeError:
        return 'error'
    
    if num_rows1 != num_rows2 or num_cols1 != num_cols2:
        return 'error'
    
    for row in range(num_rows1):
        resultMatrix.append([])
        for col in range(num_cols1):
            resultMatrix[row].append(Matrix1[row][col] + Matrix2[row][col]) 
    
    return resultMatrix
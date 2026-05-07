'''
This is an excersise to create a function that inputs two matricies
and outputs either a matrix containing the sum of the two inputed matricies
or an error to ensure that the program is able to continue running without
interuption, as well as being able to output a value such that
adding the matricies [[1,3],[2,0]] and [[0,6],[2,0]] would produce
[[1,9],[4,0]]
'''
def matrixAdd(Matrix1:list[list[float]], Matrix2:list[list[float]]):
    resultMatrix: list[list[float]] = list()
    
    if str(type(Matrix1)) != "<class 'list'>" or str(type(Matrix2)) != "<class 'list'>":
        return 'error - not a matrix'
    
    try:
        num_rows1 = len(Matrix1)
        num_rows2 = len(Matrix2)
        num_cols1 = len(Matrix1[0])
        num_cols2 = len(Matrix2[0])
    
    except TypeError:
        return "error - TypeError"

    if num_rows1 != num_rows2 or num_cols1 != num_cols2:
        return 'error - matricies are not the same'
    
    for row in range(num_rows1):
        resultMatrix.append([])
        for col in range(num_cols1):
            resultMatrix[row].append(Matrix1[row][col] + Matrix2[row][col]) 
    
    return resultMatrix
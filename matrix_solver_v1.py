example = [[1,2,6,25],[2,7,14,58],[0,2,5,19]]
example1 = [[1,2,-1,1,3],[1,1,-1,1,1],[1,3,-1,1,5]]
example2 = [[1,2,3,4,5], [3,2,1,6,7], [4,4,4,10,11], [3,6,1,6,7], [3,2,1,16,7]]

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(str(value), end=' ')
        print()
    
def input_matrix():
    matrix = []
    columns = int(input('# of columns in matrix: \n'))
    rows = int(input('# of rows in matrix: \n'))
    
    if rows < 2 or columns < 2:
        return "error"
    
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            value = int(input("Enter value for row " + str(row) + " column " + str(column) + ': \n'))
            matrix[row].append(value)
            
    return matrix

def swap_rows(matrix, row1, row2): #swap row 1 and row 2 with one another
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

def multiply_row(matrix, row, factor): #row1 * factor -> row1
    for n in range(len(matrix[row])):
        matrix[row][n] = matrix[row][n] * factor
    return matrix

def add_rows(matrix, row1, row2, coeff): #row1 + coeff*row2 -> row1
    for n in range(len(matrix[row1])):
        applied_row2 = matrix[row2][n] * coeff
        matrix[row1][n] = matrix[row1][n] + applied_row2
    return matrix

def gaussian_elimination(matrix):
    
    for column in range(len(matrix[0]) - 1):
        if matrix[column][column] == 0:
            for row in range(len(matrix)):
                if matrix[row][column] != 0:
                    swap_rows(matrix, row, column)
                    print_matrix(matrix)
                    print()
    
    for column in range(len(matrix[0]) - 1):
        for row in range(len(matrix)):
            if row != column:
                if matrix[column][column] != 0:
                    add_rows(matrix, row, column, -(matrix[row][column] / matrix[column][column]))
                    print_matrix(matrix)
                    print()

    for column in range(len(matrix[0]) - 1):
        for row in range(len(matrix)):
            if matrix[column][column] and matrix[column][row] == 0:
                multiply_row(matrix, column, 1 / matrix[column][column])
                print_matrix(matrix)
                print()
                
    return matrix


def check_for_solutions(matrix):
    pass


print(example)
print_matrix(example)
print()
example = gaussian_elimination(example)
print()
print(example)
print()
print_matrix(example)

# print(example1)
# print_matrix(example1) 
# example1 = gaussian_elimination(example1)
# print()
# print(example1)
# print()
# print_matrix(example1)

print(example2)
print_matrix(example2)
print()
example2 = gaussian_elimination(example2)
print()
print(example2)
print()
print_matrix(example2) 
 
 
#matrix1 = input_matrix()
#print(matrix1)
#print_matrix(matrix1)
#matrix1 = gaussian_elimination(matrix1)
#print()
#print(matrix1)
#print_matrix(matrix1)
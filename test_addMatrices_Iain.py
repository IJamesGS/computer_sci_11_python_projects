#see    vvv     for documentation
from addMatrices_Iain import matrixAdd

def test_matrixAdd():
    assert matrixAdd([[1,3],[2,0]], [[0,6],[2,0]]) == [[1,9],[4,0]]
    assert matrixAdd([[1,2,3],[4,5,6],[7,8,9]], [[9,8,7],[6,5,4],[3,2,1]]) == [[10,10,10],[10,10,10],[10,10,10]]
    assert matrixAdd([[1,2,3],[4,5,6],[7, 8, 9]], [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]) == [[0,0,0],[0,0,0],[0,0,0]]
    assert matrixAdd([[1,2,3],[1,2,3]], [1,2,3,4,5,6]) == "error - TypeError"
    assert matrixAdd([], []) == 'error'
    assert matrixAdd(None, None) == 'error - not a matrix'
    assert matrixAdd(2, 5) == 'error - not a matrix'
import matrix_thomasandai as m

matrix = [[1.0, 0, 3.5], [0, 6, 3]]

def test_swapRow():
    assert m.swapRow(matrix, 0, 1) == [[0, 6, 3], [1.0, 0, 3.5]]

def test_doGaussian():
    assert m.doGaussian(matrix) == ([[1.0, 0.0, 3.5], [0.0, 1.0, 0.5]], 1)
    assert m.doGaussian([[34, 5555, 1],[1, 2, 67],[333,33,3]]) == ([[1,0,67.82996172772006],[0,1,-0.4149808638600328],[0,0,-22570.6828868234]], 0)
    assert m.doGaussian([6, 12]) == ([1, 2], 1)
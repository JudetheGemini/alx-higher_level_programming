#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    myMatrix = matrix.copy()
    for i in range(len(myMatrix)):
        myMatrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (myMatrix)


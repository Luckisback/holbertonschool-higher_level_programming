#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    my_mat = matrix[:]
    line = len(my_mat)
    col = len(my_mat[0])
    for i in range(line):
        for j in range(col):
            my_mat[i][j] = matrix[i][j] ** 2
    return my_mat

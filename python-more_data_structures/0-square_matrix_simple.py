#aptitueqi/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_mat = []
    if not matrix:
        return
    for i in range(len(matrix)):
        my_mat.append(list(map(lambda x: x ** 2, matrix[i])))
    return my_mat

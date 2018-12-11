import numpy as np

def zeros_matrix(m, n):
    return [[0 for i in range(n)] for j in range(m)]


def multiply(matrix_1, matrix_2):
    result = zeros_matrix(len(matrix_1),len(matrix_2[0]))

    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
    
    return result

def add_matrix(matrix_1, matrix_2):
    row_len = len(matrix_1)
    col_len = len(matrix_1[0])

    matrix_result = zeros_matrix(row_len, col_len)

    for i in range(row_len):
        for j in range(col_len):
            matrix_result[i][j] = matrix_1[i][j] + matrix_2[i][j]
    
    return matrix_result

def substract(matrix_1, matrix_2):        
    matrix_result = zeros_matrix(len(matrix_1), len(matrix_1[0]))

    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            matrix_result[i][j] = matrix_1[i][j] - matrix_2[i][j]
    
    return matrix_result

def reshape(matrix, row_dest, col_dest):
    new_matrix = zeros_matrix(row_dest, col_dest)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix
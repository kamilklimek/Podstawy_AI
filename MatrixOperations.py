import numpy as np

def zeros_matrix(m, n):
    return [[0 for i in range(m)] for j in range(n)]


def multiply(matrix_1, matrix_2):
    n = len(matrix_1[0])
    m = len(matrix_1)
    p = len(matrix_2[0])
    result_matrix = zeros_matrix(m, p)

    for i in range(m):
        for j in range(p):
            sum = 0
            for k in range(n):
                sum += matrix_1[i][k] * matrix_2[k][j]
        result_matrix[i][j] = sum
    
    return result_matrix

def add_matrix(matrix_1, matrix_2):
    matrix_result = zeros_matrix(len(matrix_1), len(matrix_1[0]))

    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            matrix_result[i][j] = matrix_1[i][j] + matrix_2[i][j]
    
    return matrix_result

def substract(matrix_1, matrix_2):        
    matrix_result = zeros_matrix(len(matrix_1), len(matrix_1[0]))

    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            matrix_result[i][j] = matrix_1[i][j] - matrix_2[i][j]
    
    return matrix_result

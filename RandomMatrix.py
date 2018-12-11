import random

def get_random_matrix(row: int, col: int):
    random_matrix = [[0 for x in range(col)] for y in range(row)] 
    for i in range(row):
        for j in range(col):
            random_matrix[i][j] = random.random()
    
    return random_matrix
    

def get_matrix_with_value(row: int, col: int, value: int):
    random_matrix = [[0 for x in range(col)] for y in range(row)] 
    for i in range(row):
        for j in range(col):
            random_matrix[i][j] = value
    
    return random_matrix
    

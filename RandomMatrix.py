import random

def get_random_matrix(row: int, col: int):
    random_matrix = [[0 for x in range(col)] for y in range(row)] 
    for i in range(row):
        for j in range(col):
            random_matrix[i][j] = random.random()
    
    return random_matrix
    

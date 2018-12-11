import random

def get_point_by_range(range: tuple):
    min_value, max_value = range
    x = round(random.uniform(min_value, max_value),2)
    y = round(random.uniform(min_value, max_value),2)
    return x, y
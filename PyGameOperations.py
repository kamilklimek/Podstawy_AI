def resize_point_to_size(point: tuple, size: tuple):
    width, height = size
    x, y = point
    return int((x + 2) * width/10), int((y+2) * height/10)

def resize_results(results: list, size: tuple):
    output_results = []
    for result in results:
        point, one_result = result
        point = resize_point_to_size(point, size)
        output_results.append((point, one_result))
    return output_results
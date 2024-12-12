def get_cardinal_neighbour_indexes(x: int, y:int, twod_array: list[list]) -> set:
    maxX = len(twod_array)
    maxY = len(twod_array[0])
    if check_array_bounds(x, y, maxX, maxY):
        return set()
    options = set()
    options = options + [(x-1, y)] if check_array_bounds(x-1, y, maxX, maxY) else options
    options = options + [(x+1, y)] if check_array_bounds(x+1, y, maxX, maxY) else options
    options = options + [(x, y-1)] if check_array_bounds(x, y-1, maxX, maxY) else options
    options = options + [(x, y+1)] if check_array_bounds(x, y+1, maxX, maxY) else options
    return options
        

def check_array_bounds(x: int, y: int, maxX: int, maxY: int) -> bool:
    print(x, y, maxX, maxY)
    if x < 0 or y < 0:
        return False
    if x >= maxX or y >= maxY:
        return False
    return True
    
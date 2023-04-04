
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # all but not diagonally

def find_root(matrix: list[list[int]]) -> tuple[int, int]:
    for i, row in enumerate(matrix):
        for j, number in enumerate(row):
            if number == 1:
                return i, j
            
    return -1, -1

def has_water_side(root, grid):
    for direction in directions:
        new_row = root[0] + direction[0]
        new_col = root[1] + direction[1]

        if new_row < 0 or \
           new_row >= len(grid) or \
           new_col < 0 or \
           new_col >= len(grid[0]) or \
           grid[new_row][new_col] == 0:
            return True

    return False

def find_perimiter_helper(grid, root, visited): 
    visited[root[0]][root[1]] = True
    perimeter = 0
    for direction in directions:
        new_row = root[0] + direction[0]
        new_col = root[1] + direction[1]

        if new_row < 0 or \
           new_row >= len(grid) or \
           new_col < 0 or \
           new_col >= len(grid[0]) or \
           grid[new_row][new_col] == 0:
        
            perimeter += 1 # there is no neighbor

        elif not visited[new_row][new_col]:
            perimeter += find_perimiter_helper(grid, (new_row, new_col), visited)

    return perimeter

def find_perimeter(grid: list[list[int]]) -> int: 
    root: tuple[int, int] = find_root(grid)
    perimeter: int = 0

    if root == (-1, -1): 
        return perimeter
    
    visited: list[list[bool]] = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    perimeter = find_perimiter_helper(grid, root, visited)

    return perimeter






if __name__ == "__main__":
    grid = [[0, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0]]
    
    print(find_perimeter(grid))
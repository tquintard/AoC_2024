from typing import Tuple
from common import create_grid, get_input


# Directions to look for neighbors: right, diagonal-down-right, down, diagonal-down-left, left, diagonal-up-left, up, diagonal-up-right
LOOK_DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def main(inputs: str) -> Tuple[int, int]:
    """
    Main function to solve the problem by finding valid positions of the words.
    """
    grid = create_grid(inputs.splitlines())  # Convert input into a grid
    nb_row = len(grid)  # Number of rows in the grid
    nb_col = len(grid[0])  # Number of columns in the grid
    pos_visited = set()
    sol1 = set()

    def pos_in_grid(x, y) -> bool:
        return 0 <= x < nb_col and 0 <= y < nb_row

    start = [(x, y) for y, row in enumerate(grid)
             for x, col in enumerate(row) if col == '^'][0]

    dx_dy = LOOK_DIR[0]
    x, y = start
    while pos_in_grid(x, y):
        if grid[y][x] != '#':
            pos_visited.add((x, y, dx_dy))
            sol1.add((x, y))
        else:
            x, y = x - dx_dy[0], y - dx_dy[1]
            dx_dy = LOOK_DIR[(LOOK_DIR.index(dx_dy) + 1) % 4]
        x, y = x + dx_dy[0], y + dx_dy[1]

    return len(sol1), 'Not yet solved'


inputs = get_input(6, "", False)
print(main(inputs))

from common import get_input, next_direction, pos_in_grid, LOOK_DIR
from typing import Tuple, List
from collections import defaultdict


def main(topo_map: str) -> Tuple[int, int]:
    grid = list()
    zero_positions = defaultdict(int)
    for y, row in enumerate(topo_map.splitlines()):
        grid.append(list())
        for x, col in enumerate(row):
            grid[y].append(int(col))
            if col == '0':
                zero_positions[(x, y)] = 0
    nb_row = len(grid)
    nb_col = len(grid[0])

    def check_next_pos():
        if pos_in_grid(x, y, nb_col, nb_row):
            if grid[y][x] == '#':
                return True
        return False

    for zero_pos in zero_positions.keys():
        # Move to the next position
        x, y = x + LOOK_DIR[0][0], y + LOOK_DIR[0][1]

    return grid, zero_pos


inputs = get_input(10, "", True)
print(main(inputs))

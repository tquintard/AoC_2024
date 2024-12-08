from typing import Tuple
from common import create_grid, get_input
from collections import defaultdict


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
    new_block = set()

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
            # look if the next position would be a new block
            block_x, block_y = x + dx_dy[0], y + dx_dy[1]
            new_look = LOOK_DIR[(LOOK_DIR.index(dx_dy) + 1) % 4]
            x_, y_ = x, y
            new_visited = set()
            while pos_in_grid(x_, y_):
                if grid[y_][x_] != '#':
                    new_visited.add((x_, y_, new_look))
                    if (x_, y_, new_look) in pos_visited:
                        new_block.add((block_x, block_y))
                        break
                else:
                    x_, y_ = x_ - new_look[0], y_ - new_look[1]
                    new_look = LOOK_DIR[(LOOK_DIR.index(new_look) + 1) % 4]
                print(len(new_block))
                x_, y_ = x_ + new_look[0], y_ + new_look[1]
                if (x_, y_, new_look) in new_visited:
                    # new_block.add((block_x, block_y))
                    break

        else:
            x, y = x - dx_dy[0], y - dx_dy[1]
            dx_dy = LOOK_DIR[(LOOK_DIR.index(dx_dy) + 1) % 4]
        x, y = x + dx_dy[0], y + dx_dy[1]

    # for pos in pos_visited.keys():
    #     x, y = start
    #     grid[pos[1]][pos[0]] = '#'
    #     while pos_in_grid(x, y):
    #         if grid[y][x] != '#':

    #             pos_visited[(x, y)].append(dx_dy)

    #         else:
    #             x, y = x - dx_dy[0], y - dx_dy[1]
    #             dx_dy = LOOK_DIR[(LOOK_DIR.index(dx_dy) + 1) % 4]
    #         x, y = x + dx_dy[0], y + dx_dy[1]

    return len(sol1), len(new_block)


inputs = get_input(6, "", True)
print(main(inputs))

# # look if the next position would be a new block
# block_x, block_y = x + dx_dy[0], y + dx_dy[1]
# new_look = LOOK_DIR[(LOOK_DIR.index(dx_dy) + 1) % 4]
# x_, y_ = x, y
# while pos_in_grid(x_, y_):
#     if grid[y_][x_] != '#':
#         if new_look in pos_visited[(x_, y_)]:
#             new_block.add((block_x, block_y))
#             break
#     else:
#         x_, y_ = x_ - new_look[0], y_ - new_look[1]
#         new_look = LOOK_DIR[(LOOK_DIR.index(new_look) + 1) % 4]
#     x_, y_ = x_ + new_look[0], y_ + new_look[1]
#     print("     ", x_, y_)

from typing import List, Tuple
from os.path import dirname, join

# Directions for neighbor look-up: up, right, down, left
LOOK_DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# Directions to look for neighbors: right, diagonal-down-right, down, diagonal-down-left, left, diagonal-up-left, up, diagonal-up-right
FULL_LOOK_DIR = [(1, 0), (1, 1), (0, 1), (-1, 1),
                 (-1, 0), (-1, -1), (0, -1), (1, -1)]


def create_grid(inputs: List):
    grid = list()
    for line in inputs:
        grid.append(list(line))
    return grid, len(grid), len(grid[0])


def pos_in_grid(x: int, y: int, nb_col: int, nb_row: int) -> bool:
    """ Check if the position (x, y) is within the bounds of the grid """
    return 0 <= x < nb_col and 0 <= y < nb_row


def next_direction(current_dir: Tuple, directions: List[Tuple]) -> Tuple:
    """
    Get the next direction in a cyclic list of directions.
    """
    return directions[(directions.index(current_dir) + 1) % len(directions)]


def next_position(pos: Tuple[int, int], dx_dy: Tuple[int, int]) -> Tuple[int, int]:
    return map(sum, zip(pos, dx_dy))


def get_input(day: int, separator: str = '\n', sample: bool = False) -> List[str]:
    """
    Read input data from a file for a given day of Advent of Code.

    Args:
    - day (int): The day for which input data is required.
    - separator (str, optional): The separator used to split lines in the file. Defaults to newline.

    Returns:
    - List[str]: A list containing lines from the input file.
    """

    # Construct the file path based on the day
    input_file_path = join(
        dirname(__file__), f'../../input{"/sample" if sample else ""}/Day_{day}.txt')

    # Open the input file and read its contents
    with open(input_file_path, 'r') as file:
        # Read the file content, strip any trailing spaces or newlines, and split lines based on the separator
        return file.read().rstrip().split(separator) if separator else file.read().rstrip()

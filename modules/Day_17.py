<<<<<<< HEAD
=======
from typing import List
from .crucible import min_heat


def main(grid: List[str]) -> List[int]:
    # reformat the grid in a list of integer
    grid = [list(map(int, line)) for line in grid]
    return min_heat(grid, 1, 3), min_heat(grid, 4, 10)
>>>>>>> c1892ee19846c666ca88ca7597d997cd51b8f5f5

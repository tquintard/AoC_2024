from typing import Tuple, List
from modules.common import create_grid

# Directions to look for neighbors: right, diagonal-down-right, down, diagonal-down-left, left, diagonal-up-left, up, diagonal-up-right
LOOK_DIR = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

def find_loc(grid: List[str], char: str) -> List[Tuple[int, int]]:
    """
    Find all positions of a given character in the grid.
    """
    return [(x, y) for y, row in enumerate(grid) for x, col in enumerate(row) if col == char]

def look_next(act_loc: Tuple[int, int], act_char_idx: int, dx_dy: Tuple[int, int], 
              grid: List[str], nb_row: int, nb_col: int, locs_ok: List[Tuple[int, int]], 
              word: str) -> Tuple[int, int]:
    """
    Recursively checks if the next character of the word exists in the given direction.
    """
    x, y = act_loc[0] + dx_dy[0], act_loc[1] + dx_dy[1]
    # Check if the next position is within bounds and matches the next character
    if 0 <= x < nb_col and 0 <= y < nb_row and grid[y][x] == word[act_char_idx + 1]:
        locs_ok.append((x, y))  # Append valid position
        if act_char_idx < len(word) - 2:  # Continue checking next characters
            look_next((x, y), act_char_idx + 1, dx_dy, grid, nb_row, nb_col, locs_ok, word)
    # Return the position of A if the entire word is matched
    if len(locs_ok) == len(word):
        return locs_ok[-2]

def find_words(grid: List[str], nb_row: int, nb_col: int, char: str, 
               word: str, look_dir: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Finds all valid positions for a given word starting with a specific character in the grid.
    """
    valid_pos = []  # Stores valid positions for the word
    locs = find_loc(grid, char)  # Find all starting locations of the character
    for loc in locs:
        for dir in look_dir:
            a_pos = look_next(loc, 0, dir, grid, nb_row, nb_col, [loc], word)
            if a_pos:  # Append valid position if the word is found
                valid_pos.append(a_pos)
    return valid_pos

def main(inputs: str) -> Tuple[int, int]:
    """
    Main function to solve the problem by finding valid positions of the words.
    """
    grid = create_grid(inputs.splitlines())  # Convert input into a grid
    nb_row = len(grid)  # Number of rows in the grid
    nb_col = len(grid[0])  # Number of columns in the grid
    
    # Find positions for "XMAS" starting with "X"
    sol1_pos = find_words(grid, nb_row, nb_col, "X", "XMAS", LOOK_DIR)
    
    # Find positions for "MAS" starting with "M" in specific directions
    sol2_pos = find_words(grid, nb_row, nb_col, "M", "MAS", LOOK_DIR[1::2])
    
    # Count unique diagonal positions for "MAS"
    a_diag_pos_unique = set(sol2_pos)
    
    # Return counts: number of "XMAS" and the difference in "MAS" counts
    return len(sol1_pos), len(sol2_pos) - len(a_diag_pos_unique)

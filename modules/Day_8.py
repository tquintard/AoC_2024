from typing import List, Tuple, Callable
import sys
import re
from collections import defaultdict, Counter, deque

infile = r'C:\Users\Thomas\Desktop\Scripts\AoC_2024\input\Day_7.txt'
p1 = 0
p2 = 0
D = open(infile).read().strip()


# Define the possible operations (example: add, subtract, multiply, etc.)
OPS: List[Callable[[List[int]], int]] = [
    lambda nums: nums[0] + nums[1],  # Example: addition
    lambda nums: nums[0] - nums[1],  # Example: subtraction
    lambda nums: nums[0] * nums[1],  # Example: multiplication
    # Add other operations as necessary
]


def calc_partial_result(result: int, operands: List[int], part: int) -> bool:
    """
    Recursively checks if the operands can be combined using the allowed 
    operations up to the given part to produce the target result.

    Args:
        result (int): Target result to achieve.
        operands (List[int]): List of integers to combine.
        part (int): Maximum index of operations to consider from OPS.

    Returns:
        bool: True if the result can be achieved, False otherwise.
    """
    # Base case: If only one operand is left, check if it matches the result
    if len(operands) == 1:
        return operands[0] == result

    # Try all operations from OPS up to the given part
    for op in OPS[:part + 1]:
        # Apply the operation on the first two operands and recurse
        new_operands = [op(operands[:2])] + operands[2:]
        if calc_partial_result(result, new_operands, part):
            return True

    # If no operation leads to the result, return False
    return False


def main(inputs: str) -> Tuple[int, int]:
    """
    Processes a series of equations and calculates the sum of results for 
    which the operands can be combined to match the result using 
    different subsets of operations.

    Args:
        inputs (str): Multiline string of equations in the format "result = operands".

    Returns:
        Tuple[int, int]: Two sums, one for each level of partial evaluation.
    """
    equations = inputs.splitlines()
    sol = [0, 0]  # Initialize sums for part 1 and part 2

    for eq in equations:
        # Parse the result and operands from the equation
        result, *operands = map(int, re.findall(r"(\d+)", eq))

        # Evaluate for each part (1 and 2) and add to the corresponding sum
        for part in (1, 2):
            if calc_partial_result(result, operands, part):
                sol[part - 1] += result

    return tuple(sol)


print(p1)
print(p2)

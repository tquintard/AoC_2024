import logging
from os.path import dirname, join
from typing import List
from math import gcd


def create_grid(inputs: list):
    grid = list()
    for line in inputs:
        grid.append(list(line))
    return grid


def transpose(grid):
    return [*zip(*grid)]


def reverse(_list: list) -> list:
    return _list[::-1]


def lcm(*args: int):
    if len(args) < 2:
        raise ValueError("At least two integers are required.")

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    result = args[0]
    for i in range(1, len(args)):
        result = lcm(result, args[i])

    return result


def is_power2(num: int) -> bool:
    return num > 0 and (num & (num - 1)) == 0


def init_log():
    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    log_file = '../app.log'
    file_handler = logging.FileHandler(log_file, mode='w')
    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def print_grid(logger, grid: list) -> None:
    for row in grid:
        logger.debug(''.join(row))


def print_log(logger, msg: object) -> None:
    logger.debug(msg)

<<<<<<< HEAD
=======
from typing import List
from .bricks import Bricks as B


def main(inputs: List[str]) -> List[str]:
    B.bricks = [B(line) for line in inputs]
    B.bricks_fall()
    return B.desintegrate(), B.chain_reaction()
>>>>>>> c1892ee19846c666ca88ca7597d997cd51b8f5f5

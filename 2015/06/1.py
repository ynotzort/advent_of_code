import fileinput
from typing import Callable
import numpy as np

data = fileinput.input()

def on(_: int) -> int:
    return 1

def off(_: int) -> int:
    return 0

def toggle(v: int) -> int:
    return 1-v

def parse_command(line: str):
    match line.split(" "):
        case ["turn", "on", coords1, "through", coords2]:
            return (on, coords1.split(','), coords2.split(','))
        case ["turn", "off", coords1, "through", coords2]:
            return (off, coords1.split(','), coords2.split(','))
        case ["toggle", coords1, "through", coords2]:
            return (toggle, coords1.split(','), coords2.split(','))
        case _:
            raise ValueError("parsing failed")

def apply_to_grid(grid: np.array, operation: Callable[[int], int], from_t, to_t) -> np.array:
    assert len(grid.shape) == 2
    w,h = grid.shape
    assert w > to_t[0]
    assert h > to_t[1]

    for x in range(from_t[0], to_t[0]+1):
        for y in range(from_t[1], to_t[1]+1):
            grid[x, y] = operation(grid[x, y])

    return grid
    

grid = np.zeros((1000,1000))
for line in data:
    line = line.strip()
    cmd, c1, c2 = parse_command(line)
    c1 = tuple(map(int, c1))
    c2 = tuple(map(int, c2))
    grid = apply_to_grid(grid, cmd, c1, c2)
    # print(cmd, c1, c2)

print(np.sum(grid))

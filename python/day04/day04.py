from collections import defaultdict
from itertools import compress
import os
import time
import re


def findWordPart1(grid, pos, word):
    slopes = [complex(0, 1), complex(1, 1), complex(1, 0), complex(1, -1)]

    return sum(
        "".join([grid[pos + i * s] for i in range(len(word))]) == word for s in slopes
    )


def findWordPart2(grid, pos):
    if grid[pos] != "A":
        return
    posSlope, negSlope = complex(1, 1), complex(1, -1)
    return (
        (grid[pos + posSlope] == "S" and grid[pos - posSlope] == "M")
        or (grid[pos + posSlope] == "M" and grid[pos - posSlope] == "S")
    ) and (
        (grid[pos + negSlope] == "S" and grid[pos - negSlope] == "M")
        or (grid[pos + negSlope] == "M" and grid[pos - negSlope] == "S")
    )


def main():

    # input
    print(os.getcwd())
    day = "04"
    year = "2024"
    input_file = f"./inputs/day{day}.txt"
    print(input_file)
    part1, part2 = 0, 0
    levels = []

    with open(input_file) as f:
        # groups = f.read().split('\n')
        lines = f.read().splitlines()

    # calc
    start_time = time.time()
    searchTerm = "XMAS"

    # compute the grid
    grid = defaultdict(str)
    rows, cols = len(lines), len(lines[0])

    for y in range(rows):
        for x in range(cols):
            grid[complex(x, -y)] = lines[y][x]

    # part1
    part1 = sum(
        (
            findWordPart1(grid, complex(x, -y), searchTerm)
            + findWordPart1(grid, complex(x, -y), searchTerm[::-1])
        )
        for x in range(cols)
        for y in range(cols)
    )

    # part2
    part2 = sum(
        (int(findWordPart2(grid, complex(x, -y)) or 0))
        for x in range(cols)
        for y in range(cols)
    )

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )
    

if __name__ == "__main__":
    main()

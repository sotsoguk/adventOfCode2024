from collections import Counter
from itertools import compress
import os
import time
import heapq


def safe(level):
    firstDiff = [t - s for s, t in zip(level, level[1:])]
    return (
        all([y <= -1 for y in firstDiff]) and all([y >= -3 for y in firstDiff])
    ) or (all([y >= 1 for y in firstDiff]) and all([y <= 3 for y in firstDiff]))


def safe2(level):
    for i in range(len(level) - 1):
        if not (1 <= level[i + 1] - level[i] <= 3):
            return safe(level[:i] + level[i + 1 :]) or safe(
                level[: i + 1] + level[i + 2 :]
            )
    return True


def main():

    # input
    print(os.getcwd())
    day = "02"
    year = "2024"
    input_file = f"./inputs/day{day}.txt"
    print(input_file)
    part1, part2 = 0, 0
    levels = []

    with open(input_file) as f:
        # groups = f.read().split('\n')
        lines = f.read().splitlines()

    for l in lines:
        level = list(map(int, l.split()))
        levels.append(level)

    # calc
    start_time = time.time()

    # part1
    safeList1 = list(map(safe, levels))
    part1 = sum(safeList1)
    # only process unsafe lists in part2
    unsafeList1 = list(compress(levels, [not elem for elem in safeList1]))

    # part2
    p2list = list(map(lambda l: (safe2(l) or safe2(l[::-1])), unsafeList1))
    part2 = sum(p2list) + part1

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()

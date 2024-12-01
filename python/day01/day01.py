from collections import Counter
import os
import time
import heapq


def main():

    # input
    print(os.getcwd())
    day = "01"
    year = "2024"
    input_file = f"./inputs/day{day}.txt"
    # print(input_file)
    part1, part2 = 0, 0
    leftList, rightList = [], []

    with open(input_file) as f:
        # groups = f.read().split('\n')
        lines = f.read().splitlines()

    for l in lines:
        a, b = list(map(int, l.split("   ")))
        leftList.append(a)
        rightList.append(b)

    counterLeft, counterRight = Counter(leftList), Counter(rightList)

    # calc
    start_time = time.time()
    part1 = sum(
        map(
            lambda tuple: abs(tuple[0] - tuple[1]),
            zip(sorted(leftList), sorted(rightList)),
        )
    )

    part2 = sum([counterLeft[el] * el * counterRight[el] for el in counterLeft])

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()

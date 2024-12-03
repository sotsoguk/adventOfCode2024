from itertools import compress
import os
import time
import re


def main():

    # input
    print(os.getcwd())
    day = "03"
    year = "2024"
    input_file = f"./inputs/day{day}.txt"
    print(input_file)
    part1, part2 = 0, 0
    levels = []

    with open(input_file) as f:
        # groups = f.read().split('\n')
        lines = f.read().splitlines()

    input = "".join(lines)
    # calc
    start_time = time.time()

    # part1
    pattern1 = r"mul\((\d*),(\d*)\)"
    part1 = sum(map(lambda x: int(x[0]) * int(x[1]), re.findall(pattern1, input)))

    # part2
    pattern2 = r"mul\((\d*),(\d*)\)|(do\(\))|(don't\(\))"
    parsePart2 = re.findall(pattern2, input)

    factor = 1
    for elem in parsePart2:
        a, b, c, d = elem
        if a and b:
            part2 += factor * int(a) * int(b)
        elif c:
            factor = 1
        elif d:
            factor = 0

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()

from collections import defaultdict
import functools
import os
import time


def main():

    # input
    print(os.getcwd())
    day = "05"
    year = "2024"
    input_file = f"./inputs/day{day}.txt"
    print(input_file)
    part1, part2 = 0, 0
    levels = []

    with open(input_file) as f:
        groups = f.read().split("\n\n")
        # lines = f.read().splitlines()

    # calc
    start_time = time.time()
    rules, updates = defaultdict(set), []

    for r in groups[0].split("\n"):
        a, b = map(int, r.split("|"))
        rules[a].add(b)

    for u in groups[1].split("\n"):
        updates.append(list(map(int, u.split(","))))

    # custom comparator if a in rules[b] => a>b
    def compareRules(x, y):
        if x in rules[y]:
            return 1
        if y in rules[x]:
            return -1

    # part1 & part2
    for u in updates:
        uSorted = sorted(u, key=functools.cmp_to_key(compareRules))
        if uSorted == u:
            part1 += u[len(u) // 2]
        else:
            part2 += uSorted[len(u) // 2]

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()

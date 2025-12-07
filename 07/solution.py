import argparse
import time
from collections import deque, Counter


def read_file(fname):
    data = []
    start = None
    with open(fname, "r") as file:
        for y, line in enumerate(file):
            strip = line.strip()
            if strip != "":
                for x, c in enumerate(strip):
                    if c == "S":
                        start = complex(x, y)
                    elif c == "^":
                        data.append(complex(x, y))
                data.append(strip)
        max_y = y
    return start, data, max_y


def part_1(data):
    start, splitters, max_y = data
    hit = set()
    todo = [start]
    while todo:
        i = todo.pop()
        i += 1j
        if i.imag > max_y:
            # out of the field
            continue
        if i in splitters:
            if i in hit:
                # splitter already processed
                continue
            hit.add(i)
            todo.append(i - 1)
            todo.append(i + 1)
        else:
            todo.append(i)
    return len(hit)


def part_2(data):
    out = 0
    start, splitters, max_y = data
    hit = set()
    # BFS
    todo = [Counter([start])]
    while todo:
        line = todo.pop()
        next_line = Counter()
        for i, val in line.most_common():
            i += 1j
            if i.imag > max_y:
                # out of the field
                out += val
                continue
            if i in splitters:
                for si in [i - 1, i + 1]:
                    temp = next_line[si]
                    next_line[si] = val + temp
            else:
                temp = next_line[i]
                next_line[i] = val + temp
        if len(next_line) != 0:
            todo.append(next_line)
    return out


def main(fname):
    start = time.time()
    data = read_file(fname)
    total_1 = part_1(data)
    t1 = time.time()
    print(f"Part 1: {total_1}")
    print(f"Ran in {t1-start} s")
    total_2 = part_2(data)
    print(f"Part 2: {total_2}")
    print(f"Ran in {time.time()-t1} s")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    main(filename)

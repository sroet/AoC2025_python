import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append([int(i) for i in strip])
    return data


def part_1(data):
    out = 0
    for row in data:
        tens = -1
        idx_10 = 0
        while idx_10 < len(row) - 1:
            tens = row[idx_10]
            ones = -1
            idx = idx_10 + 1
            while idx < len(row):
                i = row[idx]
                if i > tens and idx < len(row) - 1:
                    idx_10 = idx
                    break
                if i > ones:
                    ones = i
                idx += 1
            else:
                break
        # print(f"{tens=} {ones=}")
        out += 10 * tens + ones
    return out


def part_2(data):
    out = 0
    for row in data:
        temp_out = 0
        min_idx = 0
        for i in range(11, -1, -1):
            if i == 0:
                s = slice(min_idx, None)
            else:
                s = slice(min_idx, -i)
            options = row[s]
            temp = -1
            for io, o in enumerate(options, min_idx + 1):
                if o > temp:
                    temp = o
                    min_idx = io
            temp_out += temp * 10**i
        out += temp_out
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

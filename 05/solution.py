import argparse
import time


def read_file(fname):
    ranges = []
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                ranges.append(tuple(int(i) for i in strip.split("-")))
            else:
                break
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append(int(strip))

    return ranges, data


def part_1(data):
    out = 0
    ranges, items = data
    for i in items:
        for l, r in ranges:
            if l <= i <= r:
                out += 1
                break
    return out


def make_ranges_unique(ranges):
    ranges.sort(reverse=True)
    out = []
    while ranges:
        l, r = ranges.pop()
        for lo, ro in out:
            if lo > l:
                raise ValueError("not sorted")
            if lo <= l and r <= ro:
                # full overlap
                l, r = None, None
                break
            if l > ro:
                # Not in this range
                continue
            else:
                l = ro + 1
        else:
            out.append((l, r))
    return out


def part_2(data):
    out = 0
    ranges, _ = data
    ranges = make_ranges_unique(ranges)
    for l, r in ranges:
        out += r - l + 1
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

import argparse
import time
import tqdm


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                d = strip[0]
                val = int(strip[1:])
                data.append((d, val))
    return data


def part_1(data):
    current = 50
    out = 0
    for d, val in data:
        if d == "L":
            val *= -1
        current += val
        if current % 100 == 0:
            out += 1
    return out


def part_2(data):
    current = 50
    out = 0
    for d, val in data:
        if d == "L":
            a = -1
        else:
            a = 1
        for _ in range(val):
            current += a
            if current % 100 == 0:
                out += 1
    return out


def main(fname):
    start = time.time()
    data = read_file(fname)
    total_1 = part_1(data)
    t1 = time.time()
    print(f"Part 1: {total_1}")
    print(f"Ran in {t1-start} s")
    total_2 = part_2_slow(data)
    print(f"Part 2: {total_2}")
    print(f"Ran in {time.time()-t1} s")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    main(filename)

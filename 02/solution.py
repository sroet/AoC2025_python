import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                ranges = strip.split(",")
                for r in ranges:
                    if r != "":
                        data.append(tuple(int(i) for i in r.split("-")))
    return data


def part_1(data):
    out = 0
    for l, r in data:
        len_l = len(str(l))
        len_r = len(str(r))
        if len_l % 2 != 0:
            l = int("1" + "0" * len_l)
        if len_r % 2 != 0:
            r = int("9" * (len_r - 1))
        option = str(l)[: len(str(l)) // 2]
        i_test = int(option + option)
        while i_test <= r:
            if i_test >= l:
                out += i_test
            option = str(int(option) + 1)
            i_test = int(option + option)
    return out


def part_2(data):
    out = 0
    for l, r in data:
        len_l = len(str(l))
        len_r = len(str(r))
        devisors = set(
            [
                (i, j // i)
                for j in range(len_l, len_r + 1)
                for i in range(1, j + 1)
                if j % i == 0
            ]
        )
        options = set()
        for length, times in devisors:
            if times < 2:
                continue
            for i in range(int("1" + "0" * (length - 1)), int("1" + "0" * length)):
                test = int(str(i) * times)
                if test > r:
                    break
                elif l <= test <= r:
                    options.add(test)
        for o in options:
            out += o
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

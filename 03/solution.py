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

def parts(data, digits):
    out = 0
    for row in data:
        temp_out = 0
        min_idx = 0
        for i in range(digits-1, -1, -1):
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
    total_1 = parts(data, 2)
    t1 = time.time()
    print(f"Part 1: {total_1}")
    print(f"Ran in {t1-start} s")
    total_2 = parts(data, 12)
    print(f"Part 2: {total_2}")
    print(f"Ran in {time.time()-t1} s")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    main(filename)

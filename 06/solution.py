import argparse
import time


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append(line)
        operations = data[-1]
        data = data[:-1]
    return data, operations


def part_1(data):
    out = 0
    values, operations = data
    values = [[int(i) for i in val.split()] for val in values]
    operations = operations.split()
    # do transpose
    for i, vals in enumerate(zip(*values)):
        if operations[i] == "+":
            out += sum(vals)
        else:
            temp = 1
            for v in vals:
                temp *= v
            out += temp
    return out


def part_2(data):
    out = 0
    values, operations = data
    # do transpose
    iterator = (i for i in zip(*values))
    mode = None
    for vals, op in zip(iterator, operations):
        vals = "".join(vals).strip()
        if vals.strip() == "":
            out += temp
            temp = None
            mode = None
        if op == "+":
            mode = op
            temp = 0
        elif op == "*":
            temp = 1
            mode = op
        if mode == "+":
            temp += int(vals)
        elif mode == "*":
            temp *= int(vals)
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

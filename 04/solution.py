import argparse
import time
import numpy as np
from scipy.signal import convolve2d


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append([1 if c == "@" else 0 for c in strip])
    return np.asarray(data)


def part_1(data):
    conv_mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    # use default boundary fillvalue of 0
    out = convolve2d(data, conv_mask, mode="same")
    filtered_out = (out < 4) & data
    out = np.sum(filtered_out)
    return out


def part_2(data):
    conv_mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    zeros = np.zeros(data.shape, dtype=int)
    temp = -1
    out = 0
    while temp != 0:
        # use default boundary fillvalue of 0
        temp_array = convolve2d(data, conv_mask, mode="same")
        filtered_out = (temp_array < 4) & data
        temp = np.sum(filtered_out)
        out += temp
        data = np.where(filtered_out, zeros, data)
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

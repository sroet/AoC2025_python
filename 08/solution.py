import argparse
import time
import numpy as np


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                data.append([int(i) for i in strip.split(",")])

    return np.asarray(data)


def parts(data, amount=10):
    diff = data[:, np.newaxis] - data[np.newaxis, :]
    dist = np.einsum("ijk, ijk->ij", diff, diff) ** 0.5
    dist[dist == 0] = np.inf
    temp = np.unravel_index(np.argsort(dist, axis=None), dist.shape)
    # only need every second as dist is symmetric
    connections = set((i,) for i in range(len(data)))
    for i, (x, y) in enumerate(zip(temp[0][::2], temp[1][::2])):
        if i == amount:
            lengths = [len(i) for i in connections]
            lengths.sort()
            out1 = lengths[-1] * lengths[-2] * lengths[-3]
        xset = [i for i in connections if x in i][0]
        yset = [i for i in connections if y in i][0]
        if xset == yset:
            continue
        else:
            new_set = tuple([i for i in xset] + [i for i in yset])
            connections.remove(xset)
            connections.remove(yset)
            connections.add(new_set)
        if len(connections) == 1:
            out2 = data[x][0] * data[y][0]
            break
    return out1, out2


def main(fname, amount):
    start = time.time()
    data = read_file(fname)
    total_1, total_2 = parts(data, amount)
    t1 = time.time()
    print(f"Part 1: {total_1}")
    print(f"Part 2: {total_2}")
    print(f"Total ran in {time.time()-start} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("amount", type=int, default=10)
    args = parser.parse_args()
    filename = args.filename
    amount = args.amount
    main(filename, amount)

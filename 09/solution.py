import argparse
import time
from itertools import combinations, pairwise


def read_file(fname):
    data = []
    with open(fname, "r") as file:
        for line in file:
            strip = line.strip()
            if strip != "":
                x, y = strip.split(",")
                data.append((int(x), int(y)))
    return data


def part_1(data):
    return int(
        max(
            abs((ix - jx) + 1) * abs((iy - jy) + 1)
            for (ix, iy), (jx, jy) in combinations(data, 2)
        )
    )


def part_2(data):
    traces = list(pairwise(data + [data[0]]))
    out = 0
    for (ix, iy), (jx, jy) in combinations(data, 2):
        area = (abs(ix - jx) + 1) * (abs(iy - jy) + 1)
        # print(f"{area=}, {(ix, iy)=}, {(jx, jy)=}")
        if area <= out:
            continue
        circ = list(pairwise([(ix, iy), (ix, jy), (jx, jy), (jx, iy), (ix, iy)]))
        for (sx, sy), (ex, ey) in traces:
            found = True
            for (csx, csy), (cex, cey) in circ:
                # if area == 30:
                #    print(f"{(csx, csy), (cex, cey)}")
                if csx == cex:
                    if sx == ex:
                        if csx == sx and (
                            min(csy, cey) < sy < max(csy, cey)
                            or min(csy, cey) < ey < max(csy, cey)
                        ):
                            # red point on line
                            break
                        else:
                            # parallel lines
                            continue
                    # out of the range
                    if csx <= min([sx, ex]) or csx >= max([sx, ex]):
                        continue
                    # found crossing
                    if min([csy, cey]) < sy < max([csy, cey]):
                        if area == 24:
                            print("found y  crossing")
                        break
                if csy == cey:
                    if sy == ey:
                        if csy == sy and (
                            min(csx, cex) < sx < max(csx, cex)
                            or min(csx, cex) < ex < max(csx, cex)
                        ):
                            # red point on line
                            break
                        else:
                            # parallel lines
                            continue
                    # out of the range
                    if csy <= min([sy, ey]) or csy >= max([sy, ey]):
                        continue
                    if min([csx, cex]) < sx < max([csx, cex]):
                        # if area == 24:
                        #    print("found x crossing")
                        #    print(f"{(csx, csy, cex, cey)=}, {(sx, sy, ex, ey)}")
                        break
            else:
                # if area == 24:
                #    print(f"Found no crossing between {((sx, sy), (ex, ey))}")
                found = False
            if found:
                # print(f"Found crossing {((csx, csy), (cex, cey))} and {((sx, sy), (ex, ey))}")
                break
        else:
            out = area
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

import sys
import time
import numpy as np
import random

random.seed(time.time())

scanners = []
cur_scanner = 0
for line in sys.stdin:
    line = line.strip()
    if len(line) < 1:
        cur_scanner += 1
        continue
    if cur_scanner >= len(scanners):
        scanners.append(set())
    x,y,z = list(map(int,line.split(',')))
    scanners[cur_scanner].add((x,y,z))

ROT_x = np.asarray([[1,0,0],[0,0,-1],[0,1,0]])
ROT_y = np.asarray([[0,0,1],[0,1,0],[-1,0,0]])
ROT_z = np.asarray([[0,-1,0],[1,0,0],[0,0,1]])
ROT_neg_x = np.matmul(np.matmul(ROT_x,ROT_x),ROT_x)
ROT_neg_y = np.matmul(np.matmul(ROT_y,ROT_y),ROT_y)
ROT_opp = np.matmul(ROT_x,ROT_x)

# Transform to each of the 6 faces
transformations = [
    lambda c: c, # identity
    lambda c: tuple(np.matmul(ROT_x, c).tolist()),
    lambda c: tuple(np.matmul(ROT_neg_x, c).tolist()),
    lambda c: tuple(np.matmul(ROT_y, c).tolist()),
    lambda c: tuple(np.matmul(ROT_neg_y, c).tolist()),
    lambda c: tuple(np.matmul(ROT_opp, c).tolist()),
]

# Rotate around the z-axis
rotate = lambda c: tuple(np.matmul(ROT_z, c).tolist())

# Translate
def translate(d):
    return lambda c: (c[0]+d[0], c[1]+d[1], c[2]+d[2])

def reduce(scanners, pos):
    s0 = scanners[0]
    # O(28*24*26^3) ~= 11M (still ok-ish)
    # 28 scanners in 24 transformations with 26 beacons each
    for s in scanners[1:]:
        # transform to each of the 24 orientations
        random.shuffle(transformations)
        for t in transformations:
            t_s = set(map(t,s0))
            c_p = set(map(t,pos))
            for i in range(4):
                if i > 0:
                    t_s = set(map(rotate,t_s))
                    c_p = set(map(rotate,c_p))
                # translate by matching points
                for p1 in t_s:
                    for p2 in s:
                        delta = (p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])
                        n_s = set(map(translate(delta),t_s))
                        n_p = set(map(translate(delta),c_p))
                        # get set intersection
                        common = set.intersection(n_s, s)
                        if len(common) >= 12:
                            s.update(n_s)
                            n_p.add(delta)
                            return scanners[1:], n_p
    return None, None

scanner_pos = set([(0,0,0)])
while scanners is not None and len(scanners) > 1:
    print(len(scanners), flush=True)
    scanners, scanner_pos = reduce(scanners, scanner_pos)

scanner_pos = list(scanner_pos)
print(len(scanners[0]), scanner_pos if scanners is not None else None)

mat_dist = lambda a,b: abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

max_dist = 0
for i, s1 in enumerate(scanner_pos[:-1]):
    for s2 in scanner_pos[i+1:]:
        max_dist = max(max_dist, mat_dist(s1,s2))
print(max_dist)

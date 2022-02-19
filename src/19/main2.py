import sys
import time
import numpy as np
import random

class Coord(object):
    def __init__(self, v, sensor=False):
        self.v = v
        self.isSensor = sensor

    def matmul(self, mat):
        return Coord(tuple(np.matmul(mat, self.v).tolist()), sensor=self.isSensor)

    def translate(self, d):
        n_c = (self.v[0]+d[0], self.v[1]+d[1], self.v[2]+d[2])
        return Coord(n_c, sensor=self.isSensor)

    def offset(self, other):
        return (other.v[0]-self.v[0], other.v[1]-self.v[1], other.v[2]-self.v[2])

    def __hash__(self):
        return hash(self.v)

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.v == other.v and self.isSensor == other.isSensor
        return False

random.seed(time.time())

scanners = []
cur_scanner = 0
for line in sys.stdin:
    line = line.strip()
    if len(line) < 1:
        cur_scanner += 1
        continue
    if cur_scanner >= len(scanners):
        scanners.append(set([Coord((0,0,0),sensor=True)]))
    x,y,z = list(map(int,line.split(',')))
    scanners[cur_scanner].add(Coord((x,y,z)))

ROT_x = np.asarray([[1,0,0],[0,0,-1],[0,1,0]])
ROT_y = np.asarray([[0,0,1],[0,1,0],[-1,0,0]])
ROT_z = np.asarray([[0,-1,0],[1,0,0],[0,0,1]])
ROT_neg_x = np.matmul(np.matmul(ROT_x,ROT_x),ROT_x)
ROT_neg_y = np.matmul(np.matmul(ROT_y,ROT_y),ROT_y)
ROT_opp = np.matmul(ROT_x,ROT_x)

# Transform to each of the 6 faces
transformations = [
    lambda c: c, # identity
    lambda c: c.matmul(ROT_x),
    lambda c: c.matmul(ROT_neg_x),
    lambda c: c.matmul(ROT_y),
    lambda c: c.matmul(ROT_neg_y),
    lambda c: c.matmul(ROT_opp),
]

# Rotate around the z-axis
rotate = lambda c: c.matmul(ROT_z)

# Translate
def translate(d):
    return lambda c: c.translate(d)

def reduce(scanners):
    s0 = scanners[0]
    # O(28*24*26^3) ~= 11M (still ok-ish)
    # 28 scanners in 24 transformations with 26 beacons each
    for s in scanners[1:]:
        # transform to each of the 24 orientations
        random.shuffle(transformations)
        for t in transformations:
            t_s = set(map(t,s0))
            for i in range(4):
                if i > 0:
                    t_s = set(map(rotate,t_s))
                # translate by matching points
                for p1 in t_s:
                    for p2 in s:
                        delta = p1.offset(p2)
                        n_s = set(map(translate(delta),t_s))
                        # get set intersection
                        common = set.intersection(n_s, s)
                        if len(common) >= 12:
                            s.update(n_s)
                            return scanners[1:]
    return None

while scanners is not None and len(scanners) > 1:
    print(len(scanners), flush=True)
    scanners = reduce(scanners)

print(len([c for c in scanners[0] if not c.isSensor]) if scanners is not None else None)

mat_dist = lambda a,b: abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

max_dist = 0
scanner_pos = [c.v for c in scanners[0] if c.isSensor]
for i, s1 in enumerate(scanner_pos[:-1]):
    for s2 in scanner_pos[i+1:]:
        max_dist = max(max_dist, mat_dist(s1,s2))
print(max_dist)

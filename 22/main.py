import sys

parse = [
    lambda x: int(x.split('..')[0]),
    lambda x: int(x.split('..')[1]),
]

cells = set()
for line in sys.stdin:
    state, coords = line.strip().split()
    state = state == "on"
    x_s, y_s, z_s = list(map(lambda x: x[2:], coords.split(",")))
    tup = (
        (parse[0](x_s), parse[0](y_s), parse[0](z_s)),
        (parse[1](x_s), parse[1](y_s), parse[1](z_s)),
    )
    if state:
        for x in range(tup[0][0], tup[1][0]+1):
            for y in range(tup[0][1], tup[1][1]+1):
                for z in range(tup[0][2], tup[1][2]+1):
                    cells.add((x,y,z))
    else:
        for x in range(tup[0][0], tup[1][0]+1):
            for y in range(tup[0][1], tup[1][1]+1):
                for z in range(tup[0][2], tup[1][2]+1):
                    cells.discard((x,y,z))
print(len(cells))

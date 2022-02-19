import sys

parse = lambda x: (int(x[0]), int(x[1]))

def line_intersect(l1, l2):
    if (l1[0] >= l2[0] and l1[0] <= l2[1]) or (l2[0] >= l1[0] and l2[0] <= l1[1]):
        return (max(l1[0],l2[0]),min(l1[1],l2[1]))
    else:
        return None

def shatter(c1, c2):
    # Get insection cubelet between c1 & c2
    # union of line intersects in x,y,z axis
    interval_x = line_intersect(c1[0], c2[0])
    interval_y = line_intersect(c1[1], c2[1])
    interval_z = line_intersect(c1[2], c2[2])
    if not interval_x or not interval_y or not interval_z: # no intersection
        return [c]
    # Start 'collapsing' c1 to this cubelet
    overlap = (interval_x, interval_y, interval_z)
    cubelets = []
    while c1 != overlap: # case of containment covered by False in 1st iteration
        if c1[0] != overlap[0]: # collapse x-axis
            if c1[0][0] < overlap[0][0]:
                cubelets.append(((c1[0][0],overlap[0][0]-1), c1[1], c1[2]))
                c1 = ((overlap[0][0],c1[0][1]), c1[1], c1[2])
            elif c1[0][1] > overlap[0][1]:
                cubelets.append(((overlap[0][1]+1,c1[0][1]), c1[1], c1[2])) 
                c1 = ((c1[0][0],overlap[0][1]), c1[1], c1[2])
        elif c1[1] != overlap[1]: # collapse y-axis
            if c1[1][0] < overlap[1][0]:
                cubelets.append((c1[0], (c1[1][0],overlap[1][0]-1), c1[2]))
                c1 = (c1[0], (overlap[1][0],c1[1][1]), c1[2])
            elif c1[1][1] > overlap[1][1]:
                cubelets.append((c1[0], (overlap[1][1]+1,c1[1][1]), c1[2])) 
                c1 = (c1[0], (c1[1][0],overlap[1][1]), c1[2])
        elif c1[2] != overlap[2]: # collapse z-axis
            if c1[2][0] < overlap[2][0]:
                cubelets.append((c1[0], c1[1], (c1[2][0],overlap[2][0]-1)))
                c1 = (c1[0], c1[1], (overlap[2][0],c1[2][1]))
            elif c1[2][1] > overlap[2][1]:
                cubelets.append((c1[0], c1[1], (overlap[2][1]+1,c1[2][1])))
                c1 = (c1[0], c1[1], (c1[2][0],overlap[2][1]))
        else:
            raise ValueError(f"Error, cubes should overlap: {c1} | {overlap}")
    return cubelets

cells = []
for line in sys.stdin:
    state, coords = line.strip().split()
    state = state == "on"
    x_s, y_s, z_s = list(map(lambda x: x[2:], coords.split(",")))
    tup = (parse(x_s.split('..')), parse(y_s.split('..')), parse(z_s.split('..')))
    new_cells = []
    for c in cells: 
        new_cells.extend(shatter(c, tup))
    if state:
        new_cells.append(tup)
    cells = new_cells

def cntCells(c):
    return (c[0][1]-c[0][0]+1)*(c[1][1]-c[1][0]+1)*(c[2][1]-c[2][0]+1)

print(sum(map(cntCells, cells)))

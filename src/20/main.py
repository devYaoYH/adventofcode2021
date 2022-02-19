import sys

encoding = sys.stdin.readline().strip()
ENCODING = []
for e in encoding:
    ENCODING.append(e == '#')

grid = []
for line in sys.stdin:
    if len(line.strip()) < 1:
        continue
    grid.append(list(line.strip()))

CELL = ('.', '#')
PIXEL = ((0,0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))

class Picture(object):
    def __init__(self, grid):
        self.inf_cell_state = False # initially '.'
        # Make deep copy
        self.init_grid = [[cell for cell in row] for row in grid]
        self.max_pt = None
        self.min_pt = None
        self.cells = {}
        for y in range(len(self.init_grid)):
            for x in range(len(self.init_grid[y])):
                self.cells[(x, y)] = self.init_grid[y][x] == '#'
                if self.cells[(x, y)]:
                    if self.max_pt is None:
                        self.max_pt = (x, y)
                    else:
                        self.max_pt = (max(self.max_pt[0], x), max(self.max_pt[1], y))
                    if self.min_pt is None:
                        self.min_pt = (x, y)
                    else:
                        self.min_pt = (min(self.min_pt[0], x), min(self.min_pt[1], y))

    def getEncoding(self, loc):
        code = ''
        for ay, ax in PIXEL:
            nx, ny = loc[0] + ax, loc[1] + ay
            adj = (nx, ny)
            if adj in self.cells:
                code += '1' if self.cells[adj] else '0'
            else:
                code += '1' if self.inf_cell_state else '0'
        return int(code, 2)

    def enhance(self):
        new_cells = {}
        new_max_pt = (self.max_pt[0], self.max_pt[1])
        new_min_pt = (self.min_pt[0], self.min_pt[1])
        for y in range(self.min_pt[1]-2, self.max_pt[1]+1):
            for x in range(self.min_pt[0]-2, self.max_pt[0]+1):
                cur_cell = ENCODING[self.getEncoding((x, y))]
                new_cells[(x, y)] = cur_cell
                if cur_cell:
                    new_max_pt = (max(new_max_pt[0], x), max(new_max_pt[1], y))
                    new_min_pt = (min(new_min_pt[0], x), min(new_min_pt[1], y))
        # NOTE: this is particular to my input, in particular, we observe that the
        #       encoding at [0] and [255] makes this flip between on/off each cycle.
        self.inf_cell_state = not self.inf_cell_state
        self.cells = new_cells
        self.max_pt = new_max_pt
        self.min_pt = new_min_pt

    def getOnCount(self):
        conut = 0
        for cell in self.cells.values():
            if cell:
                conut += 1
        return conut

    def print(self):
        print(self.min_pt, self.max_pt)
        for y in range(self.min_pt[1], self.max_pt[1]+1):
            line = ''
            for x in range(self.min_pt[0], self.max_pt[0]+1):
                if (x, y) in self.cells:
                    line += CELL[self.cells[(x, y)]]
                else:
                    line += CELL[self.inf_cell_state]
            print(line)
        print()

my_pic = Picture(grid)

# For Part 1:
'''
for i in range(2):
    my_pic.enhance()
    my_pic.print()
'''

# Part 2:
for i in range(50):
    my_pic.enhance()

print(my_pic.getOnCount())

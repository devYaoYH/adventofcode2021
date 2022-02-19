import sys
from heapq import heappush, heappop
from collections import deque

# Parse map
grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

VALID = lambda x,y: x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)

COST = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

ADJ = ((0,1),(0,-1),(1,0),(-1,0))

BLOCKED = set([(3,1),(5,1),(7,1),(9,1)])

ROOMS = {
    'A': set([(3,2),(3,3),(3,4),(3,5)]),
    'B': set([(5,2),(5,3),(5,4),(5,5)]),
    'C': set([(7,2),(7,3),(7,4),(7,5)]),
    'D': set([(9,2),(9,3),(9,4),(9,5)]),
}

ROOM_CELLS = ROOMS['A'] | ROOMS['B'] | ROOMS['C'] | ROOMS['D']

class State(object):
    def __init__(self, grid):
        self.grid = []
        self.actors = set()
        self.cost = 0
        # init
        for y, row in enumerate(grid):
            self.grid.append(row[:])
            for x, c in enumerate(row):
                if c != '.' and c != '#':
                    self.actors.add((x,y))

    # 'Completion' heuristic
    def heuCost(self):
        rooms, cost = ROOMS, COST
        score = self.cost
        for a_type in 'ABCD':
            for rx, ry in rooms[a_type]:
                if self.grid[ry][rx] != a_type:
                    # (ry-1) is min number of moves to fill
                    score += cost[a_type]*(ry-1)
        return score

    def isComplete(self):
        rooms = ROOMS
        for a_type in 'ABCD':
            for rx, ry in rooms[a_type]:
                if self.grid[ry][rx] != a_type:
                    return False
        return True    

    def getActions(self):
        valid, blocked, rooms, room_cells = VALID, BLOCKED, ROOMS, ROOM_CELLS
        cur_actions = []
        for a in self.actors:
            can_exit = a in room_cells
            a_type = self.grid[a[1]][a[0]]
            a_cost = COST[a_type]
            q = deque()
            v = set()
            q.append((a,0))
            v.add(a)
            while len(q):
                c, cost = q.pop()
                cx, cy = c
                for ax, ay in ADJ:
                    nx, ny = cx+ax, cy+ay
                    if valid(nx,ny):
                        if (nx,ny) not in self.actors and (nx,ny) not in v and self.grid[ny][nx] == '.':
                            v.add((nx,ny))
                            new_cost = cost+a_cost
                            if (nx,ny) not in blocked:
                                if (nx,ny) not in room_cells and can_exit:
                                    cur_actions.append((new_cost, (a,(nx,ny))))
                                elif (nx,ny) in rooms[a_type]:
                                    valid_room = True
                                    min_filled_y = 6
                                    for rx, ry in rooms[a_type]:
                                        if self.grid[ry][rx] != '.' and self.grid[ry][rx] != a_type:
                                            valid_room = False
                                            break
                                        # Always more optimal to move into the bottom-most cell available
                                        elif self.grid[ry][rx] == a_type and ry != cy:
                                            min_filled_y = min(min_filled_y, ry)
                                    if valid_room and ny == min_filled_y-1:
                                        cur_actions.append((new_cost, (a,(nx,ny))))
                            q.append(((nx,ny),new_cost))
        return cur_actions

    def move(self, action):
        cost, tup = action
        from_pos, to_pos = tup
        new_state = State(self.grid)
        t = new_state.grid[from_pos[1]][from_pos[0]]
        new_state.grid[from_pos[1]][from_pos[0]] = '.'
        new_state.grid[to_pos[1]][to_pos[0]] = t
        new_state.actors.discard(from_pos)
        new_state.actors.add(to_pos)
        new_state.cost = self.cost + cost
        return new_state

    def __hash__(self):
        return hash(''.join(sorted([f'{ax}{ay}{self.grid[ay][ax]}' for ax,ay in self.actors])))

    def __eq__(self, other):
        if len(set.intersection(self.actors, other.actors)) != len(self.actors):
            return False
        for a in self.actors:
            if a not in other.actors:
                return False
            if other.grid[a[1]][a[0]] != self.grid[a[1]][a[0]]:
                return False
        return True

    def __lt__(self, other):
        return id(self) < id(other)

    def print(self):
        for row in self.grid:
            print(''.join(row), flush=True)
        print(flush=True)

# Search
init_state = State(grid)

def astar(init_state):
    rnd = 0
    pq = [(0,init_state)]
    v = {}
    while len(pq):
        rnd += 1
        heu_cost, state = heappop(pq)
        if rnd % 5000 == 0:
            state.print()
        if state in v and v[state] < state.cost:
            continue
        if state.isComplete():
            return state.cost
        for action in state.getActions():
            next_state = state.move(action)
            if next_state not in v or v[next_state] > next_state.cost:
                v[next_state] = next_state.cost
                heappush(pq, (next_state.heuCost(),next_state))
    return -1

print(astar(init_state))

import sys
from heapq import heappush, heappop

grid = []
for line in sys.stdin:
  grid.append(list(map(int,list(line.strip()))))

maxX = len(grid[0])
maxY = len(grid)
new_grid = [[0 for x in range(maxX*5)] for y in range(maxY*5)]
for dx in range(5):
  for dy in range(5):
    delta = dx+dy
    for y in range(maxY):
      for x in range(maxX):
        ny, nx = dy*maxY+y,dx*maxX+x
        new_grid[ny][nx] = grid[y][x] + delta
        if new_grid[ny][nx] > 9:
          new_grid[ny][nx] -= 9

# A* search
def search(grid):
  ty, tx = len(grid)-1,len(grid[0])-1
  adj = ((0,1),(0,-1),(1,0),(-1,0))
  valid = lambda y,x: y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0])
  pq = [(0,0,(0,0))]
  v = {}
  while len(pq):
    heu, cost, cur = heappop(pq)
    y,x = cur
    if cur in v and v[cur] < cost:
      continue
    if y == ty and x == tx:
      return cost
    for ay,ax in adj:
      ny = y+ay
      nx = x+ax
      if valid(ny,nx):
        n_cost = grid[ny][nx]+cost
        n_coord = (ny,nx)
        if n_coord not in v or v[n_coord] > n_cost:
          heu_cost = abs(ny-ty) + abs(nx-tx)
          v[n_coord] = n_cost
          heappush(pq,(n_cost+heu_cost,n_cost,n_coord))
    
  return -1

print(search(new_grid))

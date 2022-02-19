import sys
from collections import deque

adj = ((1,0),(0,-1),(-1,0),(0,1))
grid = []
for row in sys.stdin:
  grid.append(list(map(int,list(row.strip()))))
valid = lambda x,y: x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)

low_pts = []
for y in range(len(grid)):
  for x in range(len(grid[y])):
    cur = grid[y][x]
    low_point = True
    for ax, ay in adj:
      nx = x+ax
      ny = y+ay
      if valid(nx, ny):
        if grid[ny][nx] <= cur:
          low_point = False
    if low_point:
      low_pts.append((y,x))

# BFS
def bfs(source, grid, v):
  #disp = [['.' for x in range(len(grid[0]))] for y in range(len(grid))]
  if source in v:
    return 0, v
  q = deque()
  v.add(source)
  q.append(source)
  basin_size = 0
  while len(q) > 0:
    y,x = q.pop()
    basin_size += 1
    #disp[y][x] = '*'
    for ax, ay in adj:
      nx = x+ax
      ny = y+ay
      if (ny,nx) not in v and valid(nx, ny) and grid[ny][nx] < 9:
        q.append((ny,nx))
        v.add((ny,nx))
  #for row in disp:
  #  print(''.join(row))
  return basin_size, v

print(f'num low points: {len(low_pts)}')

basin = [None, None, None]
visited_pts = set()
for pt in low_pts:
  cur_basin, visited_pts = bfs(pt, grid, visited_pts)
  try:
    cur_min = min(basin)
    if cur_min < cur_basin:
      for i in range(3):
        if basin[i] == cur_min:
          basin[i] = cur_basin
          break
  except:
    for i in range(3):
      if basin[i] is None:
        basin[i] = cur_basin
        break
print(basin[0]*basin[1]*basin[2])

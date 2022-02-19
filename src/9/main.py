import sys

adj = ((1,0),(0,-1),(-1,0),(0,1))
grid = []
for row in sys.stdin:
  grid.append(list(map(int,list(row.strip()))))
valid = lambda x,y: x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)

risk = 0
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
      risk += 1 + cur
print(risk)


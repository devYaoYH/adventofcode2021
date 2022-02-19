import sys

grid = []
for line in sys.stdin:
  grid.append(list(map(int,list(line.strip()))))

def propagate(new_blinky, blinky, grid):
  adj = ((0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1))
  valid = lambda x,y: x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)
  next_blinky = set()
  new_grid = [[grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))]
  for y,x in new_blinky:
    for ax,ay in adj:
      nx = x+ax
      ny = y+ay
      if valid(nx,ny) and (ny,nx) not in blinky:
        new_grid[ny][nx] += 1
        if new_grid[ny][nx] > 9:
          next_blinky.add((ny,nx))
  return new_grid, next_blinky

def turn(grid):
  blinky = set()
  # Increment
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      grid[y][x] += 1
      if grid[y][x] > 9:
        blinky.add((y,x))

  # Propagate
  grid, new_blinky = propagate(blinky, blinky, grid)
  while len(new_blinky) > 0:
    blinky.update(new_blinky)
    grid, new_blinky = propagate(new_blinky, blinky, grid)

  # Cleanup blinkies
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] > 9:
        grid[y][x] = 0
  return len(blinky), grid

def debug_grid(grid):
  for row in grid:
    print(''.join([str(row[x]) if row[x] > 0 else '.' for x in range(len(row))]))
  print()

turn_number = 0
flashes = 0
num_octopuses = len(grid[0])*len(grid)
while flashes < num_octopuses:
  flashes, grid = turn(grid)
  turn_number += 1

print(turn_number)

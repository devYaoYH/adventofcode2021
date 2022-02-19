import sys

adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cells = {}

def traverse(source, target):
  tx, ty = target
  dx = target[0]-source[0]
  dy = target[1]-source[1]
  dx = dx//abs(dx) if dx != 0 else 0
  dy = dy//abs(dy) if dy != 0 else 0
  #cells = []
  if (dx == 0 and dy == 1):
    #print(f'^ {source} -> {target}')
    cx, cy = source
    while (cx != tx or cy != ty):
      #cells.append((cx, cy))
      yield (cx, cy)
      cy += 1
  elif (dx == 0 and dy == -1):
    #print(f'v {source} -> {target}')
    cx, cy = source
    while (cx != tx or cy != ty):
      #cells.append((cx, cy))
      yield (cx, cy)
      cy -= 1
  elif (dx == 1 and dy == 0):
    #print(f'> {source} -> {target}')
    cx, cy = source
    while (cx != tx or cy != ty):
      #cells.append((cx, cy))
      yield (cx, cy)
      cx += 1
  elif (dx == -1 and dy == 0):
    #print(f'< {source} -> {target}')
    cx, cy = source
    while (cx != tx or cy != ty):
      #cells.append((cx, cy))
      yield (cx, cy)
      cx -= 1
  elif (dx != 0 and dy != 0):
    return
  yield target
  #cells.append(target)
  #print('cells:',cells)
  #return cells

overlap_pts = set()
for line in sys.stdin:
  source, target = line.strip().split(' -> ')
  sx, sy = list(map(int,source.split(',')))
  tx, ty = list(map(int,target.split(',')))
  for cell in traverse((sx, sy), (tx, ty)):
    try:
      cells[cell] += 1
    except KeyError:
      cells[cell] = 1
    if (cells[cell] > 1):
      overlap_pts.add(cell)

print(len(overlap_pts))

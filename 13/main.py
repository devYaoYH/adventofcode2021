import sys

# Dots
dots = set()
for line in sys.stdin:
  if not line.strip():
    break
  x,y = list(map(int,line.strip().split(',')))
  dots.add((x,y))

# Folds
for line in sys.stdin:
  axis, val = line.strip().split()[-1].split('=')
  val = int(val)
  new_dots = set()
  for dot in dots:
    if axis == 'y':
      if dot[1] < val:
        new_dots.add(dot)
      else:
        new_dots.add((dot[0],2*val - dot[1]))
    else:
      if dot[0] < val:
        new_dots.add(dot)
      else:
        new_dots.add((2*val - dot[0], dot[1]))
  dots = new_dots
  break

print(len(dots))

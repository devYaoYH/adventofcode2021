import sys

conut = 0
p = None
for line in sys.stdin:
  i = int(line.strip())
  if (p is None):
    p = i
    continue
  if (i > p):
    conut += 1
  p = i

print(conut)

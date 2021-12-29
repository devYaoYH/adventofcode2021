import sys

window = [None, None, None]
idx = 0
for line in sys.stdin:
  i = int(line.strip())
  window[idx%3] = i
  idx += 1
  if (idx < 3):
    continue
  print(sum(window))

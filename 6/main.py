import sys

fishes = list(map(int,sys.stdin.readline().strip().split(',')))

for i in range(256):
  children = [8 for j in range(fishes.count(0))]
  fishes = [f-1 if f > 0 else 6 for f in fishes]
  fishes.extend(children)
  #print(fishes)

print(len(fishes))

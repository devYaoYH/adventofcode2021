import sys

fishes = list(map(int,sys.stdin.readline().strip().split(',')))
fishes_dict = {i:0 for i in range(9)}
for f in fishes:
  fishes_dict[f] += 1

for i in range(256):
  num_children = fishes_dict[0]
  for j in range(8):
    fishes_dict[j] = fishes_dict[j+1]
  fishes_dict[6] += num_children
  fishes_dict[8] = num_children

print(sum([fishes_dict[i] for i in range(9)]))

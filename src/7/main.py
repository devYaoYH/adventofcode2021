import sys

crabs = list(map(int,sys.stdin.readline().strip().split(',')))

min_cost = None
for i in range(max(crabs)+1):
  tot_cost = 0
  for j in crabs:
    tot_cost += abs(j-i)*(abs(j-i)+1)/2
  if (min_cost is None):
    min_cost = tot_cost
  elif (tot_cost < min_cost):
    min_cost = tot_cost

print(min_cost)

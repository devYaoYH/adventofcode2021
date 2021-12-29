import sys

conut = None

def fold(conut, cur):
  for i, b in enumerate(cur):
    b = int(b)
    conut[i][b] += 1

for line in sys.stdin:
  l = list(line.strip())
  if (conut is None):
    conut = []
    for i in range(len(l)):
      conut.append([0,0])
  fold(conut, l)

print(conut)

gamma = ''
epsilon = ''
for tup in conut:
  if (tup[0] > tup[1]):
    gamma += '0'
    epsilon += '1'
  else:
    gamma += '1'
    epsilon += '0'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)

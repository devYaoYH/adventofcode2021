import sys

adjlist = {}

for edge in sys.stdin:
  s, t = edge.strip().split('-')
  if s not in adjlist:
    adjlist[s] = set()
  if t not in adjlist:
    adjlist[t] = set()
  adjlist[s].add(t)
  adjlist[t].add(s)

print(adjlist)

# DFS
viable_paths = set()
stack = [('start',set(['start']),'')]
while len(stack) > 0:
  node, visited, path = stack.pop()
  if node == 'end':
    print(path)
    viable_paths.add(path)
    continue
  for adj in adjlist[node]:
    if adj in visited:
      continue
    new_v = set(visited)
    if adj.islower():
      new_v.add(adj)
    stack.append((adj,new_v,f'{path}{adj}'))

print(len(viable_paths))

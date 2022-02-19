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
stack = [('start',set(['start']),'start',False)]
while len(stack) > 0:
  node, visited, path, repeated = stack.pop()
  if node == 'end':
    #print(path)
    viable_paths.add(path)
    continue
  for adj in adjlist[node]:
    next_repeat = False
    if adj in visited:
      if adj != 'start' and not repeated:
        next_repeat = True
      else:
        continue
    new_v = set(visited)
    if adj.islower():
      new_v.add(adj)
    stack.append((adj,new_v,f'{path},{adj}',next_repeat or repeated))

print(len(viable_paths))

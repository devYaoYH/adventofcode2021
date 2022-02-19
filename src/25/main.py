import sys

cucumbersEast = set()
cucumbersSouth = set()
max_x = 0
y = 0
for line in sys.stdin:
    line = line.strip()
    for x,c in enumerate(line):
        max_x = max(max_x, x)
        if c == '>':
            cucumbersEast.add((x,y))
        elif c == 'v':
            cucumbersSouth.add((x,y))
    y += 1
max_y = y
max_x += 1
print((max_x, max_y), len(cucumbersEast), len(cucumbersSouth))

steps = 0
updates = 1
while updates > 0:
    updates = 0
    new_cucumbers = set()
    for c in cucumbersEast:
        nc = ((c[0]+1)%max_x, c[1])
        if nc not in cucumbersSouth and nc not in cucumbersEast:
            new_cucumbers.add(nc)
            updates += 1
        else:
            new_cucumbers.add(c)
    cucumbersEast = new_cucumbers
    new_cucumbers = set()
    for c in cucumbersSouth:
        nc = (c[0], (c[1]+1)%max_y)
        if nc not in cucumbersSouth and nc not in cucumbersEast:
            new_cucumbers.add(nc)
            updates += 1
        else:
            new_cucumbers.add(c)
    cucumbersSouth = new_cucumbers
    steps += 1
print(steps)

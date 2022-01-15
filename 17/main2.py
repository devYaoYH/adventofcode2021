import sys

line = sys.stdin.readline().strip()

x_range, y_range = line.split(': ')[1].split(', ')
x_min, x_max = x_range[2:].split('..')
y_min, y_max = y_range[2:].split('..')
x_min, y_min, x_max, y_max = list(map(int,[x_min,y_min,x_max,y_max]))
if x_min < 0 and x_max < 0:
    x_min, x_max = -x_max, -x_min

print('target:',(x_min,x_max),(y_min,y_max), flush=True)

k = 0
cur_x = 0
k_min, k_max = None, None
while cur_x <= x_max:
    if cur_x >= x_min:
        if k_min is None:
            k_min = k
        else:
            k_max = k
    k += 1
    cur_x = k*(k+1)//2
print('minimum, maximum K:', (k_min, k_max), list(map(lambda k: k*(k+1)//2, (k_min, k_max))))

# Simulate all angles
dh_max = 0
valid_trajectories = set()
for x in range(k_min, x_max+1):
    for y in range(-y_min, y_min-2, -1):
        cur_x, cur_y = 0,0
        dx, dy = x, y
        while cur_x <= x_max and cur_y >= y_min:
            cur_x += dx
            cur_y += dy
            dx = max(0, dx-1)
            dy -= 1
            if cur_x >= x_min and cur_x <= x_max and cur_y >= y_min and cur_y <= y_max:
                dh_max = max(dh_max,y*(y+1)//2)
                valid_trajectories.add((x,y))
                break
print(len(valid_trajectories))
print(dh_max)

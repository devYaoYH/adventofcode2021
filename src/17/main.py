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

valid_counter = 0
max_h = 0
for k in range(k_min, k_max+1):
    # l <= k case
    for l in range(1000,-100,-1):
        #print(f'polling for (k={k}, l={l})', flush=True)
        dh_max = l*(l+1)//2
        t = k-l
        cur_x = k*(k+1)//2
        cur_y = dh_max - (t*(t+1)//2)
        while cur_y >= y_min:
            #print(f'  x={cur_x}, y={cur_y}')
            if cur_y <= y_max:
                max_h = max(max_h, dh_max)
                valid_counter += 1
            t += 1
            cur_y = dh_max - (t*(t+1)//2)
print(max_h)
print(valid_counter)
print((x_max - x_min + 1)*(y_max - y_min + 1) + valid_counter)

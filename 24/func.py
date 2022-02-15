from collections import defaultdict

# Restriction: w \in {1-9}
# Notes: z is strictly non-negative
#    - since add_y is always positive
#    - this implies that final step, w == accum
#      and z < 26
#    - also meaning z - 12 == w
#    - which means z \in {13-21}

def func(w, z, div_z, add_x, add_y):
    accum = z % 26
    accum += add_x
    z = int(z/div_z)
    if w == accum:
        return z
    else:
        return 26*z + w + add_y

# max depth = 13
seq = [
    lambda w,z: func(w, 0, 1, 14, 16),
    lambda w,z: func(w, z, 1, 11, 3),
    lambda w,z: func(w, z, 1, 12, 2),
    lambda w,z: func(w, z, 1, 11, 7),
    lambda w,z: func(w, z, 26, -10, 13),
    
    lambda w,z: func(w, z, 1, 15, 6),
    lambda w,z: func(w, z, 26, -14, 10),
    lambda w,z: func(w, z, 1, 10, 11),
    lambda w,z: func(w, z, 26, -4, 6),
    lambda w,z: func(w, z, 26, -3, 5),

    lambda w,z: func(w, z, 1, 13, 11),
    lambda w,z: func(w, z, 26, -3, 4),
    lambda w,z: func(w, z, 26, -9, 4),
    lambda w,z: func(w, z, 26, -12, 6),
]

def findValid(depth, possible_z, current_num):
    if depth == 8:
        return current_num, possible_z
    next_z = defaultdict(int)
    for w in range(1,10):
        for z in range(0,possible_z+1000):
            if seq[depth](w,z) == possible_z:
                next_z[z] = max(w,next_z[z])
    print(f"[{possible_z}]", next_z.items())
    results = list(map(lambda tup: findValid(depth-1, tup[0], tup[1]*(10**(13-depth)) + current_num), next_z.items()))
    # print(depth, results)
    if len(results) == 0:
        return (-1, -1)
    else:
        return max(results)

print(findValid(13, 0, 0))

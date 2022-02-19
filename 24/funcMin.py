from collections import defaultdict

# Restriction: w \in {1-9}
# Notes: z is strictly non-negative
#    - since add_y is always positive
#    - this implies that final step, w == accum
#      and z < 26
#    - also meaning z - 12 == w
#    - which means z \in {13-21}

def func(w, z, div_z, add_x, add_y):
    accum = z % 26 + add_x
    z = int(z/div_z)
    if w == accum:
        return z
    else:
        return 26*z + w + add_y

def invFunc(target_z, div_z, add_x, add_y):
    valid = []
    if div_z == 1:
        # case w == accum
        possible_w = target_z % 26 + add_x
        if possible_w > 0 and possible_w < 10:
            valid.append((target_z, possible_w))
        # case w != accum
        valid_z = target_z - add_y
        for possible_w in range(1,10):
            if (valid_z - possible_w)%26 == 0:
                possible_z = int((valid_z - possible_w)/26)
                if possible_w != possible_z % 26 + add_x:
                    valid.append((possible_z, possible_w))
    else:
        # case w == accum
        for i in range(0, min(div_z, 26)):
            possible_w = i + add_x
            if possible_w > 0 and possible_w < 10:
                valid.append((target_z*div_z + i, possible_w))
        # case w != accum
        valid_z = target_z - add_y
        for possible_w in range(1,10):
            if (valid_z - possible_w)%26 == 0:
                possible_z = int((valid_z - possible_w)/26)
                for i in range(0, min(div_z, 26)):
                    if possible_w != i + add_x:
                        valid.append((possible_z*div_z + i, possible_w))
    return valid

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

invSeq = [
    lambda z: invFunc(z, 1, 14, 16),
    lambda z: invFunc(z, 1, 11, 3),
    lambda z: invFunc(z, 1, 12, 2),
    lambda z: invFunc(z, 1, 11, 7),
    lambda z: invFunc(z, 26, -10, 13),
    
    lambda z: invFunc(z, 1, 15, 6),
    lambda z: invFunc(z, 26, -14, 10),
    lambda z: invFunc(z, 1, 10, 11),
    lambda z: invFunc(z, 26, -4, 6),
    lambda z: invFunc(z, 26, -3, 5),

    lambda z: invFunc(z, 1, 13, 11),
    lambda z: invFunc(z, 26, -3, 4),
    lambda z: invFunc(z, 26, -9, 4),
    lambda z: invFunc(0, 26, -12, 6),
]

def findValid(depth, possible_z, current_num):
    if depth == -1:
        if possible_z == 0:
            return current_num
        else:
            return None
    next_z = defaultdict(lambda: 11)
    for p_z, p_w in invSeq[depth](possible_z):
        next_z[p_z] = min(p_w, next_z[p_z])
    # print(f"[{possible_z}]", next_z.items())
    results = list(map(lambda tup: findValid(depth-1, tup[0], tup[1]*(10**(13-depth)) + current_num), next_z.items()))
    results = [r for r in results if r is not None]
    # print(depth, results)
    if len(results) == 0:
        return None
    else:
        return min(results)

print(findValid(13, 0, 0))

import sys

init_idx = list(map(int,sys.stdin.readline().strip().split()))

combi_count = {c: 0 for c in range(3,10)}
combi_count[0] = 1
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            combi_count[i+j+k] += 1

def step(roll, idx, score, player_idx):
    if roll > 0:
        idx[player_idx] = (idx[player_idx]+roll)%10
        score[player_idx] += idx[player_idx] if idx[player_idx] > 0 else 10
        if score[player_idx] >= 21:
            return ((combi_count[roll],0),(0,combi_count[roll]))[player_idx]
    future = [step(i, idx[:], score[:], (player_idx+1)%2) for i in range(3, 10)]
    return (combi_count[roll]*sum([tup[0] for tup in future]), combi_count[roll]*sum([tup[1] for tup in future]))

print(step(0, init_idx, [0,0], 1))

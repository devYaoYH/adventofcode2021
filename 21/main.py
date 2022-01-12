import sys

init_idx = list(map(int,sys.stdin.readline().strip().split()))

class Dice(object):
    def __init__(self, num_sides=100):
        self.sides = num_sides
        self.rolls = 0

class DeterministicDice(Dice):
    def __init__(self):
        super(DeterministicDice, self).__init__()
        self.cur_offset = 0

    def roll(self):
        self.rolls += 3
        cur_sum = (6 + self.cur_offset*3)%10
        self.cur_offset = (self.cur_offset+3)%10
        return cur_sum

def play(idx, dice):
    history = []
    score = [0 for i in idx]
    cur_player = 0
    while max(score) < 1000:
        history.append((idx[:], score[:]))
        idx[cur_player] = (idx[cur_player] + dice.roll())%10
        i, s = idx[cur_player], score[cur_player]
        score[cur_player] = s + (i if i > 0 else 10)
        cur_player = (cur_player + 1)%len(idx)
    print(score, dice.rolls)
    for i in range(len(history)-4,len(history)):
        print(history[i])
    return min(score)*dice.rolls

print(play(init_idx, DeterministicDice()))

d = DeterministicDice()
print([d.roll() for i in range(10)])

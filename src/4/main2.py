import sys

fin = sys.stdin

nums = list(map(int,fin.readline().strip().split(',')))
fin.readline()

def dot(arr1, arr2):
  tot = 0
  for a,b in zip(arr1, arr2):
    tot += a*b
  return tot

def mul(arr1, arr2):
  res = [0 for i in range(min(len(arr1),len(arr2)))]
  i = 0
  for a,b in zip(arr1, arr2):
    res[i] = a*b
    i += 1
  return res

board = []
cur_board = []
for line in sys.stdin:
  line = line.strip()
  if (line):
    cur_board.append(list(map(int,line.split())))
  elif (len(cur_board) > 0):
    board.append(cur_board)
    cur_board = []
if (len(cur_board) > 0):
  board.append(cur_board)

class Board(object):
  winnings = [
      [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
      [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
      [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0],
      [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
      [0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0],
      [0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
  ]
  def __init__(self, raw_grid):
    self.raw = [0 for i in range(25)]
    self.grid = {}
    for y, row in enumerate(raw_grid):
      for x, num in enumerate(row):
        idx = y*5+x
        self.raw[idx] = num
        self.grid[num] = idx
    self.filled = [0 for i in range(25)]

  def score(self, num):
    for w in Board.winnings:
      if (dot(self.filled, w) == 5):
        filled_sum = self.filledSum()
        unmarked_sum = sum(self.raw) - filled_sum
        print(self)
        return num*unmarked_sum
    return -1

  def mark(self, num):
    if (num not in self.grid):
      return -1
    self.filled[self.grid[num]] = 1
    return self.score(num)

  def filledSum(self):
    tot_sum = 0
    for y in range(5):
      for x in range(5):
        idx = y*5+x
        if (self.filled[idx]):
          print(f'{self.raw[idx]:2d} ', end='')
          tot_sum += self.raw[idx]
        else:
          print('   ', end='')
      print('')
    return tot_sum

  def __str__(self):
    _str = ''
    for y in range(5):
      for x in range(5):
        idx = y*5+x
        _str += f'{self.raw[idx]:2d} '
      _str += '\n'
    return _str

print(len(board))

def main(board):
  boardObjs = [Board(b) for b in board]
  last_win = -1
  for k, i in enumerate(nums):
    print(f'iter {k}')
    turn_scores = [bo.mark(i) for bo in boardObjs]
    boardObjs = [bo for bo in boardObjs if bo.score(i) == -1]
    if (len(turn_scores) and max(turn_scores) >= 0):
      last_win = max(turn_scores)
  return last_win

print(main(board))

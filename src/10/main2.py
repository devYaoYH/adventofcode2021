import sys

match = {
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<',
}
def score(rev_stack):
  cur_score = 0
  rev_map = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
  }
  for c in rev_stack:
    cur_score *= 5
    cur_score += rev_map[c]
  return cur_score

scores = []
for line in sys.stdin:
  autocorrect_score = 0
  corrupted = False
  stack = []
  for c in line.strip():
    if c in match:
      if match[c] != stack[-1]:
        corrupted = True
        break
      else:
        stack.pop()
    else:
      stack.append(c)
  if corrupted:
    continue
  autocorrect_score += score(stack[::-1])
  scores.append(autocorrect_score)
print(sorted(scores)[len(scores)//2])

import sys

match = {
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<',
}
score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
error_score = 0
for line in sys.stdin:
  stack = []
  for c in line.strip():
    if c in match:
      if match[c] != stack[-1]:
        error_score += score[c]
        break
      else:
        stack.pop()
    else:
      stack.append(c)
print(error_score)

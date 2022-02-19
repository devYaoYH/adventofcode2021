import sys

ans = 0
uniques = set([2,3,4,7])
for line in sys.stdin:
  _, out = line.strip().split('|')
  digits = list(map(len,out.split()))
  for d in digits:
    if d in uniques:
      ans += 1
print(ans)

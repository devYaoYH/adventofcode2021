import sys

mapping = {
  "forward": 0,
  "down": 0,
  "up": 0,
}

for line in sys.stdin:
  code, num = line.strip().split()
  mapping[code] += int(num)

print(mapping["forward"]*(mapping["down"] - mapping["up"]))

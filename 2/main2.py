import sys

state = {
  "aim": 0,
  "x": 0,
  "depth": 0,
}

def run_forward(x, s):
  s["x"] += x
  s["depth"] += x*s["aim"]

def run_up(x, s):
  s["aim"] -= x

def run_down(x, s):
  s["aim"] += x

fn = {
  "forward": lambda x: run_forward(x[0], x[1]),
  "up": lambda x: run_up(x[0], x[1]),
  "down": lambda x: run_down(x[0], x[1]),
}

for line in sys.stdin:
  code, num = line.strip().split()
  num = int(num)
  fn[code]((num, state))

print(state["x"]*state["depth"])

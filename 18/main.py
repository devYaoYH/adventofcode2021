import sys

DEBUG = False

class Snailfish(object):
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

    def add(self, other):
        new_number = Snailfish()
        new_number.left = self
        self.parent = new_number
        new_number.right = other
        other.parent = new_number
        return new_number

    def addChild(self, snailfish):
        snailfish.parent = self
        if self.left:
            self.right = snailfish
        else:
            self.left = snailfish
        return self

    def explode(self):
        if DEBUG:
            print(f'\n>>> explode: {self}')
        self.left = None
        self.right = None
        self.value = 0

    def split(self):
        if DEBUG:
            print(f'\n>>> split: {self}')
        if not self.value:
            return
        if self.value%2 == 0:
            new_val = self.value // 2
            self.left = Snailfish(value=new_val)
            self.right = Snailfish(value=new_val)
            self.left.parent = self
            self.right.parent = self
            self.value = None
        else:
            new_left = self.value // 2
            new_right = new_left + 1
            self.left = Snailfish(value=new_left)
            self.right = Snailfish(value=new_right)
            self.left.parent = self
            self.right.parent = self
            self.value = None

    def score(self):
        if self.value is not None:
            return self.value
        return 3*self.left.score() + 2*self.right.score()

    def __str__(self):
        if self.value is not None:
            return f'{self.value}'
        else:
            return f'[{self.left},{self.right}]'

def parse_literal(i, raw_string):
    num = ''
    for j, c in enumerate(raw_string[i:]):
        if c != ',' and c != ']':
            num += c
        else:
            break
    return int(num), i+j

def parse_number(number, i, raw_string):
    if i == len(raw_string):
        return number
    c = raw_string[i]
    if c == ']':
        return number, i+1
    elif c == ',':
        return parse_number(number, i+1, raw_string)
    elif c == '[':
        child, idx = parse_number(Snailfish(), i+1, raw_string)
        number.addChild(child)
        return parse_number(number, idx, raw_string)
    else:
        literal, idx = parse_literal(i, raw_string)
        number.addChild(Snailfish(value=literal))
        return parse_number(number, idx, raw_string)

def get_leftOf(number):
    cur = number
    while cur.parent and cur.parent.left == cur:
        cur = cur.parent
    cur = cur.parent
    if cur is None:
        return None
    cur = cur.left
    while cur.value is None:
        cur = cur.right
    return cur

def get_rightOf(number):
    cur = number
    while cur.parent and cur.parent.right == cur:
        cur = cur.parent
    cur = cur.parent
    if cur is None:
        return None
    cur = cur.right
    while cur.value is None:
        cur = cur.left
    return cur

def reduce(number):
    s = []
    s.append((number, 0))
    first_split = None
    while len(s):
        num, depth = s.pop()
        if depth == 4 and num.value is None:
            leftOf = get_leftOf(num)
            rightOf = get_rightOf(num)
            if leftOf:
                leftOf.value += num.left.value
            if rightOf:
                rightOf.value += num.right.value
            num.explode()
            return 'explode'
        if num.value is not None and num.value > 9 and first_split is None:
            first_split = num
            continue
        if num.value is not None:
            continue
        if num.right:
            s.append((num.right, depth+1))
        if num.left:
            s.append((num.left, depth+1))
    if first_split:
        first_split.split()
        return 'split'
    return None

def count(number):
    s = []
    s.append(number)
    v = set()
    while len(s):
        num = s.pop()
        v.add(id(num))
        if num.value is not None:
            continue
        if num.right:
            s.append(num.right)
        if num.left:
            s.append(num.left)
    return len(v)

cur_number = None
for line in sys.stdin:
    num, l = parse_number(Snailfish(), 1, line.strip())
    if cur_number is None:
        cur_number = num
    else:
        cur_number = cur_number.add(num)
    while reduce(cur_number):
        if DEBUG:
            print(count(cur_number), cur_number)
        continue

print(cur_number)
print(cur_number.score())

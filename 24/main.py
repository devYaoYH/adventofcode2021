import sys

class ALU(object):
    def __init__(self, input_buffer, output_buffer):
        self.vars = {
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
        }
        self.inst = {
            'inp': self.inp,
            'pnt': self.pnt,
            'add': self.add,
            'mul': self.mul,
            'div': self.div,
            'mod': self.mod,
            'eql': self.eql,
            'dmp': self.dmp,
        }
        self.input = input_buffer
        self.output = output_buffer
        self.program = ['inp w','pnt w']

    def inp(self, args):
        var = args[0]
        self.vars[var] = self.input.get()

    def pnt(self, args):
        var = args[0]
        if var.isalpha():
            self.output.put(self.vars[var])
        else:
            self.output.put(var)

    def add(self, args):
        v1, v2 = args
        if v2.isalpha():
            v2 = self.vars[v2]
        else:
            v2 = int(v2)
        self.vars[v1] = self.vars[v1]+v2

    def mul(self, args):
        v1, v2 = args
        if v2.isalpha():
            v2 = self.vars[v2]
        else:
            v2 = int(v2)
        self.vars[v1] = self.vars[v1]*v2

    def div(self, args):
        v1, v2 = args
        if v2.isalpha():
            v2 = self.vars[v2]
        else:
            v2 = int(v2)
        self.vars[v1] = int(self.vars[v1]/v2)

    def mod(self, args):
        v1, v2 = args
        if v2.isalpha():
            v2 = self.vars[v2]
        else:
            v2 = int(v2)
        self.vars[v1] = self.vars[v1]%v2

    def eql(self, args):
        v1, v2 = args
        if v2.isalpha():
            v2 = self.vars[v2]
        else:
            v2 = int(v2)
        self.vars[v1] = 1 if self.vars[v1] == v2 else 0

    def dmp(self, args):
        self.output.put(self.vars)

    def load_instructions(self, program):
        self.program = program

    def execute(self):
        for line in self.program:
            contents = line.split()
            inst = contents[0]
            args = contents[1:3]
            self.inst[inst](args)

class DebugInputStream(object):
    def __init__(self):
        self.input = []

    def get(self):
        in_raw = input()
        self.input.append(in_raw)
        return int(in_raw)

    def dump(self):
        print(self.input)

class DebugOutputStream(object):
    def __init__(self):
        self.output = []

    def put(self, obj):
        print(obj)
        self.output.append(obj)

    def dump(self):
        print(list(map(str, self.output)))

# Full program instructions (for verification)
"""
prog = []
with open('input', 'r') as fin:
    for line in fin:
        if line.strip() == "END":
            break
        prog.append(line.strip())
"""

# Reads (potentially) sub program from stdin
prog = []
for line in sys.stdin:
    if line.strip() == "END":
        break
    prog.append(line.strip())

oracle = ALU(DebugInputStream(), DebugOutputStream())
#oracle.load_instructions(['pnt -3', 'inp w', 'inp z', 'add w z', 'pnt w', 'mul w -1', 'div w 2', 'pnt w', 'pnt z', 'add w 100', 'mod w 2', 'eql w 0', 'pnt w'])
oracle.load_instructions(prog)
oracle.execute()

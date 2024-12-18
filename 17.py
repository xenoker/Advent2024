from AOC import getlines
from collections import Counter
IL = [x[x.find(':')+2:] for x in getlines(17)]
A0,B0,C0 = map(int,IL[:3])
L0 = list(map(int,IL[3].split(',')))

class Computer:
    def __init__(self,a0,b0,c0,l0):
        self.A = a0
        self.B = b0
        self.C = c0
        self.ops = l0
        self.opsl = len(self.ops)
        self.op = 0
        self.output = []

    def combo(self,i):
        return [0,1,2,3,self.A,self.B,self.C][i]

    def ins(self,i,o):
        if i == 0: self.A = self.A//(2**self.combo(o))
        elif i == 1: self.B = self.B ^ o
        elif i == 2: self.B = self.combo(o)%8
        elif i == 3:
            if self.A: self.op = o
            else: self.op += 2
        elif i == 4: self.B = self.B^self.C
        elif i == 5: self.output.append(self.combo(o)%8)
        elif i == 6: self.B = self.A//(2**self.combo(o))
        elif i == 7: self.C = self.A//(2**self.combo(o))            
    
    def run(self):
        while self.op < self.opsl:
            opcode, operand = self.ops[self.op],self.ops[self.op+1]
            self.ins(opcode, operand)
            if opcode != 3: self.op += 2   
        return self.output

def part1():
    return ','.join(map(str,Computer(A0,B0,C0,L0).run()))

def part2():
    a = 0
    s = 1
    sl = []
    ca = [(a,b) for a,b in enumerate(L0)]
    for i,n in ca:
        con = Counter()
        while len(con)<3:
            a += s
            r = Computer(a,0,0,L0).run()
            if len(r) <= i: continue
            con[r[i]]+=1
        m = con.most_common(1)[0][1]
        s *= m
        sl.append(m)
    rot = Counter(sl).most_common(1)[0][0]
    w = [[0]]
    for le in range(1,len(L0)+1):
        w.append([])
        for a in w[-2]:
            for da in range(rot):
                a2 = rot*a+da
                if Computer(a2,0,0,L0).run() == L0[-le:]:
                    w[-1].append(a2)
    return min(w[-1])

if __name__ == '__main__':
    assert part1()=="2,1,3,0,5,2,3,7,1"
    assert part2()==107416732707226

from AOC import get
from itertools import combinations
I,L = get(24).split('\n\n')
I = [tuple(i.split(': ')) for i in I.split('\n')]
L = [tuple(l.replace(' ->','').split()) for l in L.split('\n')]
AK = sorted(x[3] for x in L if x[3][0]=='z')
D0 = dict((a,bool(int(b))) for a,b in I)
OP = dict((d,(a,b,c)) for a,b,c,d in L)

def get(a, D=D0, D2=OP):
    if a in D: return D[a]
    if a not in D2: return None
    b,c,d = D2[a]
    if c == 'AND': D[a] = get(b,D=D) & get(d,D=D)
    if c == 'OR':  D[a] = get(b,D=D) | get(d,D=D)
    if c == 'XOR': D[a] = get(b,D=D) ^ get(d,D=D)
    return D[a]

def part1():
    return int(''.join('01'[get(x)] for x in reversed(AK))  ,2)

def part2():
    OPOR = list()
    for a,(b,c,d) in OP.items():
        if c == 'OR': OPOR.extend([b,d])
    S = set()
    for a,(b,c,d) in OP.items():
        if c == 'XOR':
            if a in OPOR or not any(x[0] in 'xyz' for x in (a,b,d)): S.add(a)
        if c == 'AND':
            if a not in OPOR and set((b,d))-{'x00','y00'}: S.add(a)
        if c == 'OR':
            if a[0] == 'z' and a !=AK[-1]: S.add(a)
    return ','.join(sorted(S))

if __name__ == '__main__':
    assert part1()==59619940979346
    assert part2()=="bpt,fkp,krj,mfm,ngr,z06,z11,z31"

from AOC import get
from functools import cmp_to_key
T = get(5)
R,P = T.split('\n\n')
R = [tuple(map(int,r.split('|'))) for r in R.split('\n')]
P = [ list(map(int,p.split(','))) for p in P.split('\n')]
RD = dict()
for a,b in R: RD[a] = RD.get(a,[]) + [b]

def part1_2():
    S, S2 = 0, 0
    for p in P:
        p2 = sorted(p, key=cmp_to_key(lambda a,b:[0,-1][b in RD.get(a,[])]))
        if p == p2: S += p[int(len(p)/2)]
        else: S2 += p2[int(len(p)/2)]
    return S, S2      

if __name__ == '__main__':
    assert part1_2() == (5732,4716)


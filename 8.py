from AOC import grid
from itertools import combinations
G = grid(8)
V = set(v for v in G.values() if v != '.')
L = list(tuple(xy for xy,a in G.items() if a==v) for v in V)

def part(num):
    S = set()
    for xyl in L:
        for a,b in combinations(xyl,2):
            dx,dy = a[0]-b[0], a[1]-b[1]
            for i in num == 1 and [1] or range(50):
                c = (a[0]+dx*i,a[1]+dy*i)
                if c in G: S.add(c)
                else: break
            for i in num == 1 and [1] or range(50):
                d = (b[0]-dx*i,b[1]-dy*i)
                if d in G: S.add(d)
                else: break
    return len(S)

if __name__ == '__main__':
    assert part(1)==381
    assert part(2)==1184

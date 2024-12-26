from AOC import get
from itertools import product

T = get(25).split('\n\n')
K, L = [], []
for t in T:
    [K,L][t[0]=='#'].append([t[x::6].count('#')-1 for x in range(5)])

def part1():
    return sum(all((a+b)<=5 for a,b in zip(l,k)) for l,k in product(L,K))

if __name__ == '__main__':
    assert part1()==3483


from AOC import getlines
from functools import cache
L = getlines(19)
P, T = L[0].split(', '), L[1:]

@cache
def tested(t): return sum(test(t))

def test(t):
  for p in P:
    if p == t: yield 1
    elif t.startswith(p): yield tested(t[len(p):])

def part1(): return sum(1 for x in T if tested(x))
def part2(): return sum(tested(x) for x in T)

if __name__ == '__main__':
    assert part1()==240
    assert part2()==848076019766013

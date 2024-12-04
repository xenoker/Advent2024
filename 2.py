from AOC import sget
from itertools import pairwise
L = sget(2, int, lines=True)

def check(l):
    s = set(a-b for a,b in pairwise(l))
    if s <= {1,2,3} or s <= {-1,-2,-3}: return True
    return False

def part1():
    return sum(check(l) for l in L)

def part2():
    S = 0
    for l in L:
        for rem in range(len(l)):
            l2 = l[:rem] + l[rem+1:]
            if check(l2):
                S+=1; break
    return S

if __name__ == '__main__':
    assert part1()==369
    assert part2()==428   

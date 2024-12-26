from AOC import getlines
from collections import Counter
from functools import cache
L = [int(x) for x in getlines(22)]

@cache
def mixp(s,v): return (v^s)%16777216

@cache
def next(s):
    s = mixp(s,s*64)
    s = mixp(s,s//32)
    s = mixp(s,s*2048)
    return s

def nth(s0,n):
    s = s0
    for i in range(n):
        s = next(s)
    return s

def part1():
    return sum( nth(n,2000) for n in L)

def part2():
    CC = Counter()
    for n0 in L:
        temp = []
        checked = set()
        n = n0
        for i in range(2000):
            n2 = next(n)
            seq = tuple(temp)
            if i>3 and seq not in checked:
                CC[seq] += n%10
                checked.add(seq)
            temp = temp[-3:] + [n2%10 - n%10]
            n = n2
    return max(CC.values())

if __name__ == '__main__':
    assert part1()==16999668565
    assert part2()==1898       

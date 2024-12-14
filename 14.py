from AOC import getlines, showgrid
from collections import defaultdict
from functools import reduce
PV = [tuple(map(int,l[2:].replace('v=',',').split(','))) for l in getlines(14)]
W, H = 101, 103
WM,HM = W//2, H//2

def part1():
    Q = defaultdict(int)
    for x,y,vx,vy in PV:
        x2, y2 = (x+vx*100)%W, (y+vy*100)%H
        if x2==WM or y2==HM: continue
        Q[x2>WM,y2>HM] += 1
    return reduce(lambda a,b:a*b, Q.values())

def part2():
    for dt in range(10000):
        D,S = dict(),0
        for x,y,vx,vy in PV:
            x2, y2 = (x+vx*dt)%W, (y+vy*dt)%H
            D[(x2,y2)] = '*'
            if (x2,y2-1) in D or (x2,y2+1) in D: S += 1
        if S>100:
            showgrid(D,W,H)
            return dt

if __name__ == '__main__':
    assert part1()==215987200
    assert part2()==8050

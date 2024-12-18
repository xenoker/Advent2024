from AOC import getlines, D4
from heapq import heapify, heappop, heappush
from collections import defaultdict
L = getlines(18)
B = [tuple(map(int,x.split(','))) for x in L]
S,E = (0,0),(70,70)

class Dijkstra:
    def __init__(self, mapd, start, end):
        self.MAP = mapd
        self.START = start
        self.END = end
    def search(self, p1):
        px, py = p1
        for dx,dy in D4:
            yield (px+dx,py+dy)
    def solve(self): 
        Q = [(0, self.START)]
        heapify(Q)
        self.COST = defaultdict(lambda:999999999999)
        while Q:
            cost, p1 = heappop(Q)
            for p2 in self.search(p1):
                if p2 not in self.MAP: continue
                if self.MAP.get(p2) == True: continue
                if cost+1 < self.COST[(p2)] :
                    self.COST[(p2)] = cost+1
                    heappush(Q, (cost+1, p2))
        return self.COST[self.END]

def part1():
    M = dict(((x,y),((x,y) in B[:1024])) for x in range(E[0]+1) for y in range(E[1]+1))
    return Dijkstra(M,S,E).solve()

def part2():
    l,h = 1024,len(B)
    while h-l>1:
        m = (l+h)//2
        M = dict(((x,y),((x,y) in B[:m])) for x in range(E[0]+1) for y in range(E[1]+1))
        if Dijkstra(M,S,E).solve() < 999999: l = m
        else: h = m
    return B[l]

if __name__ == '__main__':
    assert part1()==326
    assert part2()==(18,62)

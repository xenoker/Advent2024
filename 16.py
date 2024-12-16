from AOC import grid
from heapq import heapify, heappop, heappush
from collections import defaultdict, deque
G = grid(16)
S = [xy for xy,c in G.items() if c=='S'][0]
E = [xy for xy,c in G.items() if c=='E'][0]

class Dijkstra:
    def __init__(self, mapd, start, end):
        self.MAP = mapd
        self.START = start
        self.END = end

    def search(self, p1, f1):
        px, py = p1
        for dx,dy,f2 in [(1,0,0),(0,1,1),(-1,0,2),(0,-1,3)]:
            d = abs(f1-f2)
            if d==2: continue
            c = 1 + (d==3 and 1 or d)*1000
            yield (px+dx,py+dy,f2,c)
    def solve(self): 
        Q = [(0, self.START,0)]
        heapify(Q)
        self.COST = defaultdict(lambda:999999999999)
        while Q:
            cost, p1,f = heappop(Q)
            for x2,y2,f2,dc in self.search(p1,f):
                p2=x2,y2
                if p2 not in self.MAP: continue
                if self.MAP.get(p2) == '#': continue
                dcost = cost+dc
                if dcost < self.COST[(p2,f2)] :
                    self.COST[(p2,f2)] = dcost
                    heappush(Q, (dcost, p2, f2))
        self.ENDS = [(k,c) for k,c in self.COST.items() if k[0]==self.END]
        ans = min(c for k,c in self.ENDS)
        self.ENDS = [(k,c) for k,c in self.ENDS if c==ans]
        return ans
    
    def rsearch(self, p1, f1):
        px, py = p1
        dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][(f1+2)%4]
        for f2 in range(4):
            d = abs(f1-f2)
            if d==2: continue
            c = 1 + (d>0)*1000
            yield (px+dx,py+dy,f2,c)
    def rsolve(self):
        P = set([k[0] for k,c in self.ENDS])
        P.add(self.START)
        Q = deque([k for k,c in self.ENDS])
        while Q:
            p2,f2 = Q.popleft()
            for x1,y1,f1,dc in self.rsearch(p2,f2):
                p1 = x1,y1
                if p1 not in self.MAP: continue
                if self.MAP.get(p1) == '#': continue
                if self.COST[(p1,f1)] + dc == self.COST[(p2,f2)]:
                    P.add(p1)
                    Q.append((p1,f1))
        for p in P: self.MAP[p] = 'O'
        return len(P)

D = Dijkstra(G,S,E)
def part1(): return D.solve()
def part2(): return D.rsolve()

if __name__ == '__main__':
    assert part1()==109496
    assert part2()==551

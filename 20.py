from AOC import grid, D4
from collections import Counter

G = grid(20)
S = [xy for xy,c in G.items() if c=='S'][0]
E = [xy for xy,c in G.items() if c=='E'][0]

class Path:
    def __init__(self, mapd, start, end):
        self.MAP = mapd
        self.START = start
        self.END = end
        
    def search(self, p1):
        px, py = p1
        for dx,dy in D4:
            yield (px+dx,py+dy)
            
    def travel(self):
        p1 = self.START
        self.DIST = dict()
        self.DIST[self.START] = 0
        while p1 != self.END:
            for p2 in self.search(p1):
                if p2 not in self.MAP: continue
                if self.MAP.get(p2) == '#': continue
                if p2 in self.DIST: continue
                self.DIST[p2] = self.DIST[p1]+1
                p1 = p2
                break
        self.PATH = list(self.DIST.items())
        return self
    
    def msearch(self, p1, dist):
        px, py = p1
        for dx in range(-dist,dist+1):
            for dy in range(-(dist-abs(dx)),dist+1-abs(dx)):
                if dx == 0 and dy==0: continue
                yield ((px+dx, py+dy), abs(dx)+abs(dy))
                
    def cheats(self, maxm, minc):
        CC = Counter()
        UC = set()
        for p1,d1 in self.PATH:
            for p2,md in self.msearch(p1,maxm):
                if p2 not in self.DIST: continue
                if (p1,p2) in UC: continue
                d2 = self.DIST[p2]
                cut = abs(d1-d2)-md
                if cut < minc: continue
                UC.add((p2,p1))
                CC[cut] += 1
        return CC.total()

D = Path(G,S,E).travel()
def part1(): return D.cheats(2,100)
def part2(): return D.cheats(20,100)

if __name__ == '__main__':
    assert part1()==1378                
    assert part2()==975379

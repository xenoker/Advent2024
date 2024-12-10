from heapq import heapify, heappop, heappush
from AOC import grid
G = grid(10,int)
S = [xy for xy,h in G.items() if h==0]

class Hiker:
    def __init__(self, start):
        self.START = start
        self.ENDS = []
        
    def look(self, p1):
        px, py = p1
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            yield (px+dx,py+dy)

    def hike(self): 
        Q = [self.START]
        heapify(Q)
        while Q:
            p1 = heappop(Q)
            for p2 in self.look(p1):
                if p2 not in G: continue
                if not G[p1]+1==G[p2]: continue
                if G[p2] == 9: self.ENDS.append(p2)
                else: heappush(Q, p2)
        return len(set(self.ENDS)), len(self.ENDS)

trails = [Hiker(xy).hike() for xy in S]

def part1():
    return sum(t[0] for t in trails)

def part2():
    return sum(t[1] for t in trails)

if __name__ == '__main__':
    assert part1()==624
    assert part2()==1483

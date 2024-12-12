from heapq import heapify, heappop, heappush
from AOC import grid, D4
G = grid(12)

class Regioner:
    def __init__(self, start):
        self.START = start
        self.squares = set()
        self.perim = set()
        self.N = 0
        self.run()
    def look(self, p1):
        px, py = p1
        for dx,dy in D4:
            yield (px+dx,py+dy)
    def add(self, a, b, flip=False):
        if not flip: return (a[0]+b[0],a[1]+b[1])
        return (a[0]+b[1],a[1]+b[0])
    def run(self): 
        Q = [self.START]
        self.letter = G[self.START]
        heapify(Q)
        while Q:
            self.N += 1
            p1 = heappop(Q)
            self.squares.add(p1)
            for p2 in self.look(p1):
                if p2 in self.squares: continue
                elif p2 not in G or self.letter!=G[p2]: self.perim.add((p1,p2))
                elif p2 not in Q: heappush(Q, p2)
    def sides(self):
        S = 0
        for d in D4:
            side = set()
            for xy in (a for a,b in self.perim):
                if (dxy:=self.add(xy,d)) not in self.squares: side.add(dxy)
            unside = set()
            for xy in side:
                dxy = self.add(xy,d,True)
                while dxy in side:
                    unside.add(dxy)
                    dxy = self.add(dxy,d,True)
            S += len(side) - len(unside)
        return S
    def price1(self): return len(self.perim)*len(self.squares)
    def price2(self): return self.sides()*len(self.squares)

def part1_2():
    S1,S2 = 0,0
    todo = set(G.keys())
    while todo:
        R = Regioner(todo.pop())
        todo -= R.squares
        S1 += R.price1()
        S2 += R.price2()
    return S1,S2
    
if __name__ == '__main__':
    p1,p2 = part1_2()
    assert p1==1457298
    assert p2==921636

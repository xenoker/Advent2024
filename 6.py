from AOC import grid
G = grid(6)
P0X,P0Y = [xy for xy,c in G.items() if c=='^'][0]
dirs = [(0,-1),(1,0),(0,1),(-1,0)]

def traverse(x, y, d=0, tx=0, ty=0):
    P, P2, PH = set(), set(), set()
    while True:
        if tx and (x,y,d) in P: return True
        P.add((x,y,d))
        x2, y2 = x+dirs[d][0], y+dirs[d][1]
        f = G.get((x2,y2))
        if x2==tx and y2==ty: f = '#'
        if not f and not tx: return P,P2
        if not f and tx: return False
        if f != '#' :
            if not tx and (x2,y2) not in PH and traverse(x,y,d,x2,y2): P2.add((x2,y2))
            x,y = x2,y2
        else: d = (d+1)%4
        PH.add((x,y))

P1,P2 = traverse(P0X,P0Y)

def part1():
    return len(set((x,y) for x,y,d in P1))

def part2():
    return len(P2)

if __name__ == '__main__':
    assert part1()==4647
    assert part2()==1723    

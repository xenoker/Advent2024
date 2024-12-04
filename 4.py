from AOC import grid
D = grid(4)

def part1():
    S = 0
    for x,y in (xy for xy,t in D.items() if t=='X'):
        for dx,dy in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            if ''.join(D.get((x+dx*m,y+dy*m),'') for m in range(1,4)) == "MAS": S+=1
    return S

def part2():
    S = 0
    for x,y in (xy for xy,t in D.items() if t=='A'):
        for dx,dy in [(1,-1),(1,1)]:
            if ''.join(D.get((x+dx*m,y+dy*m),'') for m in [-1,0,1]) not in ['SAM','MAS']: break
        else: S+=1
    return S

if __name__ == '__main__':
    assert part1()==2567
    assert part2()==2029


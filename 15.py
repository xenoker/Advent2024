from AOC import grid, get, D4
from collections import deque
T = get(15)
MAP,DIR = T.split('\n\n')
MAP = grid(MAP,filt='@O#')
DIR = DIR.replace('\n','')
P0 = [xy for xy,t in MAP.items() if t=='@'][0]
MAP.pop(P0)
DXY = dict(zip('^>v<',D4))

def slide1(m,p,dxy):
    C = []
    for i in range(1,99):
        p2 = p[0]+dxy[0]*i, p[1]+dxy[1]*i
        p3 = p[0]+dxy[0]*(i+1), p[1]+dxy[1]*(i+1)
        if p2 not in m:
            while C:
                a,b = C.pop()
                m[b] = m.pop(a)
            return True
        if m[p2] == '#': return False
        C.append((p2,p3))
def part1():
    M = MAP.copy()
    p = P0
    for d in DIR:
        dxy = DXY[d]
        p2 = p[0]+dxy[0], p[1]+dxy[1]
        if p2 not in M: p = p2
        elif M[p2] == '#': pass
        elif slide1(M,p,dxy): p = p2
    return sum(100*xy[1]+xy[0] for xy,c in M.items() if c=='O' )


def slide2(m,p,dy):
    todo = deque([(p[0],p[1]+dy)])
    tomove = deque()
    while todo:
        t = todo.popleft()
        tc = m.get(t)
        if tc == '#': return False
        if not tc: continue
        s = (t[0]+{'[':1,']':-1}[tc],t[1])
        f = (t[0],t[1]+dy)
        if s not in tomove and s not in todo: todo.appendleft(s)
        if f not in todo and f not in tomove: todo.append(f)
        tomove.append(t)
    while tomove:
        a = tomove.pop()
        b = a[0],a[1]+dy
        m[b] = m.pop(a)
    return True
def part2():
    M = dict()
    for xy,c in MAP.items():
        pi1 = xy[0]*2, xy[1]
        pi2 = xy[0]*2+1, xy[1]
        M[pi1] = c=='O' and '[' or c
        M[pi2] = c=='O' and ']' or c
    p = P0[0]*2,P0[1]
    for d in DIR:
        dxy = DXY[d]
        p2 = p[0]+dxy[0], p[1]+dxy[1]
        if p2 not in M: p = p2
        elif M[p2] == '#': pass
        elif not dxy[1] and slide1(M,p,dxy): p = p2
        elif dxy[1] and slide2(M,p,dxy[1]): p = p2
    return sum(100*xy[1]+xy[0] for xy,c in M.items() if c=='[' )

if __name__ == '__main__':
    assert part1()==1318523
    assert part2()==1337648

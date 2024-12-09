from AOC import get
data = list(map(int,get(9)))
U,E = data[0::2], data[1::2]+[0]
assert len(U)==len(E)

def part1():
    L = []
    for iu,e in zip(enumerate(U),E):
        i,u = iu
        L.extend([i]*u)
        L.extend([-1]*e)
    ep = [i for i,v in enumerate(L) if v==-1]
    while ep and ep[0]<len(L):
        e = L.pop(-1)
        if e == -1: continue
        L[ep.pop(0)]=e
    return sum(i*idi for i,idi in enumerate(L) if idi!=-1)

def part2():
    L, ES, FS = [], [], []
    for iu,e in zip(enumerate(U),E):
        i,u = iu
        FS.append([u,len(L)])
        L.extend([i]*u)
        if e: ES.append((e,len(L)))
        L.extend([-1]*e)
    for n,p in reversed(FS):
        ep = next((i for i,es in enumerate(ES) if es[0]>=n),-1)
        if ep<0: continue
        ne,pe = ES[ep]
        if pe>p: continue
        L[pe:pe+n] = L[p:p+n]
        L[p:p+n] = [-1]*n
        if n==ne: ES.pop(ep)
        else:
            d = ne-n
            ES[ep] = (d,pe+n)
    return sum(i*idi for i,idi in enumerate(L) if idi!=-1)

if __name__ == '__main__':
    assert part1()==6330095022244
    assert part2()==6359491814941

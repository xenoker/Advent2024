from AOC import getlines
import numpy as np
L = getlines(13)
BA,BB,PXY = L[0::3],L[1::3],L[2::3]
def nums(t): return tuple(map(int,''.join(c for c in t if c.isdigit() or c == ',').split(',')))
M = [(nums(a),nums(b),nums(p)) for a,b,p in zip(BA,BB,PXY)]

def part(part=1):
    S = 0
    for A,B,P in M:
        if part==2: P = (P[0]+10000000000000, P[1]+10000000000000)
        a = np.array([[A[0],B[0]],[A[1],B[1]]],dtype=np.int64)
        b = np.array([P[0],P[1]],dtype=np.int64)
        an,bn = np.linalg.solve(a,b)
        an,bn = int(round(an,4)),int(round(bn,4))
        if an*A[0]+bn*B[0] != P[0]: continue
        if an*A[1]+bn*B[1] != P[1]: continue
        S += 3*an+bn
    return S

if __name__ == '__main__':
    assert part(1)==31761
    assert part(2)==90798500745591

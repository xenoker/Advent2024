from AOC import getlines
import sympy as sy
L = getlines(13)
BA,BB,PXY = L[0::3],L[1::3],L[2::3]
def nums(t): return tuple(map(int,''.join(c for c in t if c.isdigit() or c == ',').split(',')))
M = [(nums(a),nums(b),nums(p)) for a,b,p in zip(BA,BB,PXY)]

def part(part=1):
    S = 0
    for A,B,P in M:
        if part==2: P = (P[0]+10000000000000, P[1]+10000000000000)
        a,b = sy.symbols('a,b')
        eq1 = sy.Eq(a*A[0]+b*B[0],P[0])
        eq2 = sy.Eq(a*A[1]+b*B[1],P[1])
        sol = sy.solve([eq1,eq2],(a,b))
        an,bn = sol[a], sol[b]
        if not an.is_integer or not bn.is_integer: continue
        S += 3*an+bn
    return S

if __name__ == '__main__':
    assert part(1)==31761
    assert part(2)==90798500745591

from functools import cache
from collections import Counter
from AOC import get
L = list(map(int,get(11).split()))

@cache
def step(n):
    if n == 0: return (1,)
    elif not len(strn:=str(n))%2:
        mid = len(strn)//2
        return(int(strn[:mid]),int(strn[mid:]))
    return (n*2024,)
    
def steps(S):
    A = Counter(L)
    for s in range(S):
        B = Counter()
        for i,n in A.items():
            for ni in step(i): B[ni] += n
        A = B
    return A.total()

if __name__ == '__main__':
    assert steps(25)==231278
    assert steps(75)==274229228071551

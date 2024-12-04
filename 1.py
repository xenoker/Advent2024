from AOC import sget
L = sget(1, int)
A, B = sorted(L[::2]), sorted(L[1::2])

def part1():
    return sum(abs(a-b) for a,b in zip(A,B))

def part2():
    return sum(a*B.count(a) for a in A)

if __name__ == '__main__':
    assert part1()==2192892
    assert part2()==22962826

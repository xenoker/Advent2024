from AOC import get
from re import findall
T = get(3)

def part1():
    return sum(int(a)*int(b) for a,b in findall(r"mul\((\d+)\,(\d+)\)",T))

def part2():
    S, do = 0, True
    for a,b,c,d in findall(r"(?:(do)\(\))|(?:(don)\'t\(\))|(?:mul\((\d+)\,(\d+)\))",T):
        if a or b: do = a and True or False
        elif do and c and d: S += int(c)*int(d)
    return S   

if __name__ == '__main__':
    assert part1()==183669043
    assert part2()==59097164


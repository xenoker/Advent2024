from AOC import getlines
from operator import add,mul
from itertools import product
L, EQ = getlines(7), []
for l in L:
    a,b = l.split(': ')
    EQ.append((int(a),tuple(map(int,b.split()))))

def math(nums, ops, res):
    pops = product(ops, repeat=len(nums)-1)
    for funl in pops:
        R = nums[0]
        stack = zip(funl, nums[1:])
        for op,b in stack:
            R = op(R,b)
            if R > res: break
        if R == res: return True

def part1():
    return sum(res for res,nums in EQ if math(nums,(add, mul), res))

def part2():
    def cat(a,b): return int(f"{a}{b}")
    return sum(res for res,nums in EQ if math(nums,(add, mul, cat), res))

if __name__ == '__main__':
    assert part1()==66343330034722
    assert part2()==637696070419031


from AOC import getlines
from collections import defaultdict
from itertools import combinations
L = [tuple(l.split('-')) for l in getlines(23)]
D = defaultdict(set)
for a,b in L:
    D[a].add(b)
    D[b].add(a)

def part1():
    S3 = set()
    for a,b in D.items():
        for c,d in combinations(b,2):
            if c in D[d]:
                tri = [a,c,d]
                if any(x[0]=='t' for x in tri):
                    S3.add(tuple(sorted(tri)))
    return len(S3)

def kerbosch(graph, todo, seen=set(), done=set()):
    if not todo and not seen: return [done]
    cq = []
    for v in todo.copy():
        cq.extend(kerbosch(graph, todo&graph[v], seen&graph[v], done|{v}))
        todo-={v}
        seen.add(v)
    return cq

def part2():
    S = kerbosch(D, set(D.keys()))
    S.sort(key=len, reverse=True)
    return ','.join(sorted(S[0]))

if __name__ == '__main__':
    assert part1()==1170
    assert part2()=="bo,dd,eq,ik,lo,lu,ph,ro,rr,rw,uo,wx,yg"

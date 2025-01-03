import os
from sys import argv
from collections import defaultdict

def get(i):
    with open(f'./inputs/{i}.txt') as f:
        return f.read()
    
def sget(i, func=str, sep=None, lines=False):
    L = []
    for line in get(i).split('\n'):
        if lines: L.append(list(map(func,line.split(sep))))
        else: L.extend(map(func,line.split(sep)))
    return L

def getlines(i, func=str, emptys=False):
    return [func(x) for x in get(i).split('\n') if x or emptys]

def grid(i, func=str, default=str, filt=[]):
    text = '\n' in str(i) and i or get(i)
    D = defaultdict(default)
    for j,line in enumerate(text.split('\n')):
        for i,txt in enumerate(line):
            if filt and txt not in filt: continue
            D[(i,j)] = func(txt)
    return D

def showgrid(D,W,H,f=' '):
    for y in range(H):
        print(''.join(str(D.get((x,y),f))[0] for x in range(W)))


D8 = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
D4 = [(0,-1),       (1,0),      (0,1),       (-1,0)]

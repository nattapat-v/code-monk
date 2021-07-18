from itertools import groupby

def group(h):
    h.sort()
    h = [len(list(j)) for i, j in groupby(h)]
    h.sort()
    return h

def solution(h):
    if len(set(h)) == 1:
        print('-1')
    else:
        h = group(h)
        print(h[-1] - h[0])

T = int(input())

for _ in range(T):
    n = int(input())
    h = list(map(int, input().split()))
    solution(h)
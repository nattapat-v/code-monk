import sys

def minimum_and_xor_or(a, n):
    a.sort()

    min_val = sys.maxsize

    for i in range(n-1):
        val = (a[i] and a[i+1]) ^ (a[i] or a[i+1])
        min_val = min(min_val, val)

    print(min_val)

T = int(input())
a = []

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    minimum_and_xor_or(a, n)
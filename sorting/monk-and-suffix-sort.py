s, k = input().split()
s = [c for c in s]

suffices = []

for i in range(len(s)):
    suffices.append(s[i:])

suffices.sort()
result = suffices[int(k) - 1]

print(''.join([r for r in result]))
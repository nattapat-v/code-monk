n = int(input())
l = []

for i in range(n):
    l.append(input())

    if i == 0:
        print('0')
        continue

    cnt = 0
    for j in range(len(l) - 1):
        if l[j] < l[i]:
           cnt += 1

    print(cnt)
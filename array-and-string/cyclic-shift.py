def cyclic_shift(s):
    b_list = [s]

    prev_s = s

    while(1):
        crr_s = prev_s[1:] + prev_s[0]

        if crr_s == s:
            break
        else:
            b_list.append(crr_s)
            prev_s = crr_s

    ans = max(b_list)
    ans_idx = b_list.index(ans)
    print(ans_idx + (ans_idx + 1))

T = int(input())

for _ in range(T):
    n, k = input().split()
    s = input()
    cyclic_shift(s)
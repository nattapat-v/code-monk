def insertion_sort(l):
    result = l

    for i in range(len(l)):
        k = l[i]
        j = i

        while(j > 0 and result[j - 1] > k):
            result[j] = result[j - 1]
            j -= 1
        result[j] = k
    return result

n = int(input())
l = list(map(int, input().split()))
print(insertion_sort(l))
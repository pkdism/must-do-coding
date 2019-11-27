for _ in range(int(input())):
    n1, n2, n3 = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    a3 = list(map(int, input().split()))

    i, j, k = 0, 0, 0
    s = set()
    while i < n1 and j < n2 and k < n3:
        if a1[i] == a2[j] and a2[j] == a3[k]:
            s.add(a1[i])
        elif a1[i] < a2[j]:
            i += 1
        elif a2[j] < a3[k]:
            j += 1
        else:
            k += 1
    if len(s) == 0:
        print(-1)
    else:
        for i in s:
            print(i, end = ' ')
        print('')

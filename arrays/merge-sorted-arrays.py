for _ in range(int(input())):
    m, n = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    b = []
    i, j = 0, 0
    while i < m and j < n:
        if a1[i] < a2[j]:
            b.append(a1[i])
            i += 1
        else:
            b.append(a2[j])
            j += 1
        if i == m and j < n:
            b.append(a2[j])
            j += 1
        if i < m and j == n:
            b.append(a1[i])
            i += 1
    res1, res2 = [], []
    k = 0
    while k < m + n:
        if k < m:
            res1.append(b[k])
        else:
            res2.append(b[m + n - k])
    print(res1)
    print(res2)
    

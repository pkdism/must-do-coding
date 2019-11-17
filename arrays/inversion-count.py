for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    inv_cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                inv_cnt += 1
    print(inv_cnt)

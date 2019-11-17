for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    start = 0
    res = []
    while start < n:
        while start < n-1 and a[start + 1] < a[start]:
            start += 1
        # print('start = ', start)
        i = start + 1
        while i < n and a[i] > a[i - 1]:
            i += 1
        if start != i-1:
            res.append(tuple([start, i-1]))
        start = i
    for k in res:
        print("(",k[0], ' ', k[1], ')', end = ' ', sep = '')
    if len(res) == 0:
        print('No Profit')
    print('')

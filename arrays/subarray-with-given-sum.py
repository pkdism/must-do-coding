for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    start = 0
    cur_sum = a[0]
    flag = 0
    for i in range(n):
        if cur_sum == s:
            print(start + 1, i + 1)
            flag = 1
            break
        elif cur_sum > s:
            while cur_sum > s:
                cur_sum -= a[start]
                start += 1
        else:
            cur_sum += a[i]
    if flag == 0:
        print(-1)

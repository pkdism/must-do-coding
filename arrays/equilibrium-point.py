for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flag = 0
    arr_sum = sum(a)
    ls = 0
    for i in range(0, n):
        if ls == arr_sum - ls - a[i]:
            print(i+1)
            flag = 1
            break
        ls += a[i]
    if flag == 0:
        print(-1)

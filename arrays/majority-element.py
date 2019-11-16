for i in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    dc = {}
    flag = 0
    for el in a:
        dc[el] = dc.get(el, 0) + 1
        if dc[el] > n//2:
            flag = 1
            print(el)
            break
    if flag == 0:
        print(-1)

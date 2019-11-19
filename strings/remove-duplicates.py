for _ in range(int(input())):
    s = input()
    cnt = {}
    res = ''
    for i in s:
        if cnt.get(i, 0) == 0:
            res += chr(i)
        cnt[i] = cnt.get(i, 0) + 1
    print(res)

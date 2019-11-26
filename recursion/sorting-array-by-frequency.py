for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in a:
        cnt[i] = cnt.get(i, 0) + 1

    for k, v in sorted(cnt.items(), key = lambda kv: (-kv[1], kv[0])):
        while v > 0:
            print(k, end = ' ')
            v -= 1
    print('')

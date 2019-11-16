for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cur_max = a[n-1]
    i = n-1
    leaders = []
    while i >= 0:
        # print("el", a[i])
        if a[i] >= cur_max:
            # print(a[i], end = ' ')
            leaders.append(a[i])
            cur_max = a[i]
        i -= 1
    # print('next tc')
    for j in range(len(leaders) - 1, -1, -1):
        print(leaders[j], end = ' ')
    print('')

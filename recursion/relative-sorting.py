for _ in range(int(input())):
    m, n = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    # position = {}
    counts = {}

    # for i in range(n):
    #     if a2[i] not in position.keys():
    #         position[a2[i]] = i
    for i in range(m):
        counts[a1[i]] = counts.get(a1[i], 0) + 1

    for i in range(n):
        while counts[a2[i]] > 0:
            print(a2[i], end = ' ')
            counts[a2[i]] -= 1
    rest = []
    for i in range(m):
        if a1[i] not in a2:
            rest.append(a1[i])

    for i in sorted(rest):
        print(i, end = ' ')
    print('')

for _ in range(int(input())):
    r, c = map(int, input().split())
    mat, res = [], []
    r1, c1 = set(), set()
    for row in range(r):
        one_row = list(map(int, input().split()))
        if 1 in one_row:
            r1.set(row)
        for k in range(c1):
            if one_row[k] == 1:
                c1.add(k)

    for row in range(r):
        for col in range(r):
            if row in r1 or col in c1:
                print(1, end = ' ')
            else:
                print(0, end = ' ')
        print('')

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_sum, cur_max = 0, 0
    for i in a:
        cur_max = cur_max + i
        if cur_max < 0:
            cur_max = 0
        if cur_max > max_sum:
            max_sum = cur_max
    print(max_sum)

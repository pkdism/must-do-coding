for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    zeros, ones, twos = 0, 0, 0
    for i in a:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1
        elif i == 2:
            twos += 1
    for k in range(zeros):
        print(0, end = ' ')
    for k in range(ones):
        print(1, end = ' ')
    for k in range(twos):
        print(2, end = ' ')
    print('')
    

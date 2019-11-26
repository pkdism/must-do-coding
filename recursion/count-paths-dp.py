for _ in range(int(input())):
    r, c = map(int, input().split())
    dp = [[0]*c]*r
    for i in range(r):
        dp[i][0] = 1
    for i in range(c):
        dp[0][i] = 1
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[r-1][c-1])

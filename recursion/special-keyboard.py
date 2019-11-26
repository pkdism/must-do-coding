# def sk_output(n):
#     if n <= 6:
#         return n
#     return max(sk_output(n-1) + 1, 2*sk_output(n-3), 3*sk_output(n-4), 4*sk_output(n-5))
for _ in range(int(input())):
    n = int(input())
    # print(sk_output(n))
    if n > 75:
        print(-1)
    dp = [0]*(n + 1)
    for i in range(min(n+1, 7)):
        dp[i] = i
    if n >= 7:
        for i in range(min(7, n+1), n+1):
            dp[i] = max(dp[i-1] + 1, 2*dp[i-3], 3*dp[i-4], 4*dp[i-5])

    print(dp[n])

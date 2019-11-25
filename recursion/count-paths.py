def possible_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return possible_paths(m - 1, n) + possible_paths(m, n - 1)


for _ in range(int(input())):
    m, n = map(int, input().split())
    print(possible_paths(m, n))

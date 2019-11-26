def ff(mat, x, y, prev_col, new_col, r, c):
    if x < 0 or y < 0 or x >= r or y >= c or mat[x][y] != prev_col or mat[x][y] == new_col:
        return
    mat[x][y] = new_col
    ff(mat, x-1, y, prev_col, new_col, r, c)
    ff(mat, x+1, y, prev_col, new_col, r, c)
    ff(mat, x, y-1, prev_col, new_col, r, c)
    ff(mat, x, y+1, prev_col, new_col, r, c)



for _ in range(int(input())):
    r, c = map(int, input().split())
    mat = [[0]*c]*r
    for i in range(r):
        mat[i] = list(map(int, input().split()))
    x, y, k = map(int, input().split())
    prev_col = mat[x][y]
    ff(mat, x, y, prev_col, k, r, c)

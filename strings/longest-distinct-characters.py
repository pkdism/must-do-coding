for _ in range(int(input())):
    s = input()
    n = len(s)
    visited = [-1]*256
    prev = 0
    max_len = 1
    cur_len = 1
    visited[ord(s[0])] = 0
    for i in range(1, n):
        prev = visited[ord(s[i])]
        if prev == -1 and (i - cur_len > prev):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - prev
        visited[ord(s[i])] = i
    if cur_len > max_len:
        max_len = cur_len
    print(max_len)

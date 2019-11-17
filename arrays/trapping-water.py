def trappingWater(a,n):
    l, h = a[0], a[n-1]
    start, end = 0, n-1
    water = 0
    while start < n and end >= 0 and start < end:
        if l < h:
            water += max(l - a[start], 0)
            start += 1
        elif l >= h:
            water += max(h - a[end], 0)
            end -= 1
    print(water)

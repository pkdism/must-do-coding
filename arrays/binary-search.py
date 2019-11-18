def bin_search(arr, left, high, key):
    if left > high:
        return -1
    m = left + (high - left)//2
    if arr[m] == key:
        return m
    elif arr[m] > key:
        return bin_search(arr, left, m - 1, key)
    else:
        return bin_search(arr, m + 1, high, key)

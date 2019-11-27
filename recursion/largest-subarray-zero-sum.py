{
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
}
''' This is a function problem.You only need to complete the function given below '''
#Your task is to complete this function
#Your should return the required output
def maxLen(n, arr):

    # # O(n^2) solution
    # max_len = 0
    # for i in range(n):
    #     cur_sum = 0
    #     for j in range(i, n):
    #         cur_sum += arr[j]
    #         if cur_sum == 0:
    #             max_len = max(max_len, j - i + 1)
    # return max_len

    # O(n) solution
    max_len = 0
    hsh = {}
    s = 0
    for i in range(n):
        s += arr[i]
        if arr[i] == 0 and max_len == 0:
            max_len = 1
        if s == 0:
            max_len = i + 1
        if s in hsh:
            max_len = max(max_len, i - hsh[s])
        else:
            hsh[s] = i
    return max_len

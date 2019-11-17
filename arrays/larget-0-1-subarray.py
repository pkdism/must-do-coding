''' This is a function problem.You only need to complete the function given below '''
# Your task is to complete this function
# Function should return an integer
def maxLen(n, lis):
    # if n == 0:
    #     return 0
    # ones = sum(lis)
    # zeros = n - ones
    # if zeros == ones:
    #     return n
    # else:
    #     return max(maxLen(n-1, lis[1:]), maxLen(n-1, lis[:-1]))
    for i in range(n):
        if lis[i] == 0:
            lis[i] = -1

    min, max = 1000000, -1
    sums = 0
    for i in range(n):
        sum += lis[i]
        if sum == 0:
           if i <= min:
               min = i
           elif i >= max:
               max = i
    return max - min

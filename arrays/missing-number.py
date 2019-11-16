n = int(input())
total_sum = n*(n+1)//2
a = map(int, input().split())
array_sum = sum(a)
print(total_sum - array_sum)

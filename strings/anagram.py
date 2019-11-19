def anagram(a, b):
    if len(a) != len(b):
        return 'NO'
    val = 0
    for i in range(len(a)):
        val = val ^ ord(a[i])
        val = val ^ ord(b[i])
    if val == 0:
        return 'YES'
    else:
        return 'NO'

for _ in range(int(input())):
    a, b = map(str, input().split())
    print(anagram(a, b))

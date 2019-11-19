from itertools import permutations

for _ in range(int(input())):
    s = input()
    for k in sorted(permutations(s)):
        print(''.join(k), end = ' ')
    print('')

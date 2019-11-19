for _ in range(int(input())):
    roman = input()
    mapping = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    seq = 'MDCLXVI'
    n = len(roman)
    res = 0
    i = 0
    while i < n:
        val = mapping[roman[i]]
        if i+1 < n:
            val2 = mapping[roman[i+1]]
            if val >= val2:
                res = res + val
                i += 1
            else:
                res = res + val2 - val
                i += 2
        else:
            res += val
            i += 1
    print(res)

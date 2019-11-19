for _ in range(int(input())):
    orig = input()
    rot = input()
    n = len(orig)
    if len(rot) != n:
        print(0)
    else:
        if (orig == rot[2:] + rot[:2]) or (orig == rot[(n-2):] + rot[:(n-2)]):
            print(1)
        else:
            print(0)

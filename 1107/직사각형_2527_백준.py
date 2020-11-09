for _ in range(4):
    a0, a1, a2, a3, a4, a5, a6, a7 = map(int, input().split())
    if a3 < a5 or a2 < a4 or a1 > a7 or a0 > a6:
        result = 'd'
    elif (a3 == a5 and (a0 == a6 or a2 == a4)) or (a1 == a7 and (a0 == a6 or a2 == a4)):
        result = 'c'
    elif a3 == a5 or a2 == a4 or a1 == a7 or a0 == a6:
        result = 'b'
    else:
        result = 'a'
    print(result)
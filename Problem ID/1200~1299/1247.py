for _ in range(3):
    s = 0
    n = int(input())
    for i in range(n):
        s += int(input())

    if(s == 0):
        print(0)
    elif(s < 0):
        print('-')
    else:
        print('+')
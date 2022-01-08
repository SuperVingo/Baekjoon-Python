while(True):
    n = input()
    if(n == '0'):
        break

    s = 0
    for i in n:
        if(i == '0'):
            s += 4
        elif(i == '1'):
            s += 2
        else:
            s += 3
    print(s + len(n) + 1)        
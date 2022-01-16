while True:
    a = input()
    if(a == '0.00'):
        break
    a = float(a)
    n = 2
    t = 0.5
    while True:
        if(t >= a):
            break
        
        t += 1 / (n+1)
        n += 1
    print(n-1, 'card(s)')
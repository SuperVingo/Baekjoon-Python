n = int(input())
for i in range(n):
    m = int(input())
    p1 = 0
    p2 = 0

    for i in range(m):
        line = input().split()
        if(line[0] == 'P'):
            if(line[1] == 'S'):
                p2 += 1
            elif(line[1] == 'R'):
                p1 += 1
        elif(line[0] == 'R'):
            if(line[1] == 'P'):
                p2 += 1
            elif(line[1] == 'S'):
                p1 += 1
        elif(line[0] == 'S'):
            if(line[1] == 'R'):
                p2 += 1
            elif(line[1] == 'P'):
                p1 += 1
    if(p1 == p2):
        print('TIE')
    elif(p1 > p2):
        print('Player 1')
    else:
        print('Player 2')
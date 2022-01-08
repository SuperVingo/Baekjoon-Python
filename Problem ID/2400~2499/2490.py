for _ in range(3):
    line = list(map(int, input().split()))
    if(sum(list(line)) == 3):
        print('A')
    elif(sum(list(line)) == 2):
        print('B')
    elif(sum(list(line)) == 1):
        print('C')
    elif(sum(list(line)) == 0):
        print('D')
    else:
        print('E')
        
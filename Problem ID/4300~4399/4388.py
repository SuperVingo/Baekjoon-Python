while True:
    line = input().split()
    if(int(line[0]) == 0 and int(line[1]) == 0):
        break

    carry = False
    cnt = 0
    leng = min(len(line[0]), len(line[1]))
    for i in range(leng):
        print(int(line[0][-i-1]), int(line[1][-i-1]))
        a = int(line[0][-i-1]) + int(line[1][-i-1])
        if(carry):
            a += 1

        if(a >= 10):
            carry = True
            cnt += 1
        else:
            carry = False
        
    #if(carry):
    #    if(len(line[0]) > len(line[1])):
    #        if(int(line[0][-leng]) == 9):
    #            cnt += 1
    #    else:
    #        if(int(line[1][-leng]) == 9):
    #            cnt += 1
    print(cnt)
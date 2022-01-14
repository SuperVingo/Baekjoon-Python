while True:
    line = input().split()
    if(int(line[0]) == 0 and int(line[1]) == 0):
        break

    carry = False
    cnt = 0
    leng = max(len(line[0]), len(line[1]))
    line[0] = '0' * (leng - len(line[0])) + line[0]
    line[1] = '0' * (leng - len(line[1])) + line[1]
    for i in range(len(line[0])):
        a = int(line[0][-i-1]) + int(line[1][-i-1])
        if(carry):
            a += 1

        if(a >= 10):
            carry = True
            cnt += 1
        else:
            carry = False
        
        #print(int(line[0][-i-1]), int(line[1][-i-1]), a)
    print(cnt)
n = int(input())
lst = []
for _ in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    if(a == b and b == c):
        lst.append(10000+max(a, b, c)*1000)
    elif(a == b or b == c or a == c):
        if(a == b):
            lst.append(a*100+1000)
        elif(b == c):
            lst.append(b*100+1000)
        elif(a == c):
            lst.append(a*100+1000)
    else:
        lst.append(100*max(a,b,c))
print(max(lst))
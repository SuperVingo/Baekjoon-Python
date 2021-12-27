line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
if(a == b and b == c):
    print(10000+max(a, b, c)*1000)
elif(a == b or b == c or a == c):
    if(a == b):
        print(a*100+1000)
    elif(b == c):
        print(b*100+1000)
    elif(a == c):
        print(a*100+1000)
else:
    print(100*max(a,b,c))

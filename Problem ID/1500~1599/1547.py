a = int(input())
t = 1
for i in range(a):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    if(x == t):
        t = y
    elif(y == t):
        t = x
print(t)
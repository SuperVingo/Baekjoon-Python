n = int(input())
p1 = 100
p2 = 100
for i in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])

    if(a > b):
        p2 -= a
    elif(a < b):
        p1 -= b
print(p1)
print(p2)
n = int(input())
for _ in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = pow(a, b, 10)
    if(c == 0):
        print(10)
    else:
        print(c)

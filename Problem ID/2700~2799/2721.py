n = int(input())
for i in range(n):
    a = int(input())
    s = 0
    for j in range(1, a+1):
        s += j*(((j+1)*(j+2))//2)
    print(s)
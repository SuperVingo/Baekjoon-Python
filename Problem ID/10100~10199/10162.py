a = int(input())
if(a % 10 != 0):
    print(-1)
else:
    n = a // 300
    m = (a % 300) // 60
    s = (a % 60) // 10
    print(n, m, s)
def getnext(a):
    return a + (a % 10) + (a // 10)

n = 1
while(n < 10000):
    print(n)
    n = getnext(n)

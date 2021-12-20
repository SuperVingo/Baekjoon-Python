def getnext(a):
    return a + (a // 1000) + ((a % 1000) // 100) + ((a % 100) // 10) + (a % 10)

lst = [False] * 10000
for i in range(1, 10000):
    n = getnext(i)
    if(n < 10000):
        lst[n] = True

for i in range(1, len(lst)):
    if(not lst[i]):
        print(i)
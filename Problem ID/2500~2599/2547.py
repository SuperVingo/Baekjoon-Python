n = int(input())
for _ in range(n):
    input()
    s = 0
    m = int(input())
    for i in range(m):
        s += int(input())
    if(s % m == 0):
        print('YES')
    else:
        print('NO')
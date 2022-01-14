from re import L


while True:
    n = int(input())
    if(n == -1):
        break

    c = 0
    b = 0
    for i in range(n):
        line = list(map(int, input().split()))
        c += line[0] * (line[1]-b)
        b = line[1]
    print(c, 'miles')
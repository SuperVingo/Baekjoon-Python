n = int(input())
for _ in range(n):
    a = str(bin(int(input())))[2:]
    for i in range(len(a)):
        if(a[len(a)-i-1] == '1'):
            print(i, end=' ')
    print()
        
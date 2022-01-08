n = int(input())
for i in range(n):
    a = int(input())
    print(a//25, end=' ')
    a = a % 25
    print(a//10, end=' ')
    a = a % 10
    print(a//5, end=' ')
    a = a % 5
    print(a)
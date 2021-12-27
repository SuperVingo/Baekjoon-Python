line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
n = int(input())

c += (n % 60)
b += (n // 60)
b += (c // 60)
c %= 60
a += (b // 60)
b %= 60
a %= 24

print(a, b, c)

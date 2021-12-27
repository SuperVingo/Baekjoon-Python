line = input().split()
a = int(line[0])
b = int(line[1])
n = int(input())

b += n
a += (b // 60)
b %= 60
a %= 24

print(a, b)

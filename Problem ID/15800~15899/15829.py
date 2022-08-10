n = input()
l = list(input())

r = 0
p = 0
for i in l:
    r = r + (ord(i) - ord('a') + 1) * (31 ** p)
    p = p + 1
print(r % 1234567891)
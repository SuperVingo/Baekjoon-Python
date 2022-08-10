n = int(input())
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort(reverse=True)
print(a)
print(b)
t = 0
for i in range(len(a)):
    t = t + a[i]*b[i]
print(t)
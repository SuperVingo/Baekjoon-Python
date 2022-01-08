n = int(input())
lst = [i for i in range(n+1)]
s = 0
for i in range(len(lst)):
    for j in range(i, len(lst)):
        s += lst[i] + lst[j]
print(s)
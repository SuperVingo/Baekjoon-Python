lst = []
for _ in range(5):
    line = list(map(int, input().split()))
    lst.append(sum(line))
print(lst.index(max(lst))+1, max(lst))
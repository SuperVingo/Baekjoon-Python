num = int(input())
lst = []
for i in range(num):
    t = input()
    lst.append((len(t), t))
lst = list(set(lst))
lst = sorted(lst, key=lambda x : (x[0], x[1]))
for i in lst:
    print(i[1])
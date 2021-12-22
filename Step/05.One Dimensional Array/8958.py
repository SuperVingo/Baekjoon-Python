num = int(input())
lst = []
for i in range(num):
    lst.append(input())

for line in lst:
    point = 0
    score = 1
    for ch in line:
        if(ch == 'O'):
            point = point + score
            score = score + 1
        else:
            score = 1
    print(point)


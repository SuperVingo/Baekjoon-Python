line = input().split()
n = int(line[0])
m = int(line[1])

card = []
line = input().split()
for i in line:
    card.append(int(i))

cost = m
num = 0
if(n == 3):
    print(sum(card))
else:
    for i in range(n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                val = card[i] + card[j] + card[k]
                if(m == val):
                    print(m)
                    exit(0)
                elif(val > m):
                    continue
                elif(abs(val-m) < cost):
                    cost = abs(val-m)
                    num = val
    print(num)
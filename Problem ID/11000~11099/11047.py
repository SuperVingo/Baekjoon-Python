n, m = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

s = 0
for i in range(n):
    print(s, i, coins[i])
    if coins[i] == m:
        s = i
        break
    elif coins[i] >= m:
        s = i - 1
        break
    else:
        s = i

res = 0
for i in range(s, -1, -1):
    res = res + (m // coins[i])
    m = m % coins[i]
    if m == 0:
        break
print(res)
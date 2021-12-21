cnt = 0
def hanoi(n:int, sp:int, mp:int, dp:int):
    if(n == 0):
        return
    global cnt
    hanoi(n-1, sp, dp, mp)
    cnt += 1
    print(sp, dp)
    hanoi(n-1, mp, sp, dp)

n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 2, 3)

import sys

l_fibo0 = [0 for _ in range(41)]
l_fibo1 = [0 for _ in range(41)]
l_fibo0[0] = 1
l_fibo1[1] = 1

def fibo():
    for i in range(2, 41):
        l_fibo0[i] = l_fibo0[i-1] + l_fibo0[i-2]
        l_fibo1[i] = l_fibo1[i-1] + l_fibo1[i-2]

fibo()
n = int(sys.stdin.readline().strip())
for _ in range(n):
    m = int(sys.stdin.readline().strip())
    print(l_fibo0[m], l_fibo1[m])
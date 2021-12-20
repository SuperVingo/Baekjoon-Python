import sys

n = int(input())

for i in range(n):
    user_input = sys.stdin.readline().rstrip().split()
    a = int(user_input[0])
    b = int(user_input[1])
    print(a+b)
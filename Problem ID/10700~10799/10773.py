import sys

stack = []

n = int(input())
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if(num == 0):
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))
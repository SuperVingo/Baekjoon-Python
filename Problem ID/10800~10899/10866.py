from collections import deque

import sys

n = int(input())

queue = deque()
for i in range(n):
    l = sys.stdin.readline().strip().split()
    
    if l[0] == 'push_front':
        queue.appendleft(int(l[1]))
    if l[0] == 'push_back':
        queue.append(int(l[1]))
    elif l[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif l[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif l[0] == 'size':
        print(len(queue))
    elif l[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif l[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif l[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

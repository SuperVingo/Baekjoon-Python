k = int(input())

for i in range(k):
    line = input().split()
    h = int(line[0])
    w = int(line[1])
    n = int(line[2])

    if(n % h != 0):
        front = format(n%h)
        rear = format(int(n/h + 1), '02')
        print(front+rear)
    else:
        front = format(h)
        rear = format(int(n/h), '02')
        print(front+rear)
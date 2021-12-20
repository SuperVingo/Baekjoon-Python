n = int(input())

case = 1
for i in range(n):
    line = input().split()
    n1 = int(line[0])
    n2 = int(line[1])
    print("Case #%d: %d + %d = %d" % (case, n1, n2, n1 + n2))
    case = case + 1
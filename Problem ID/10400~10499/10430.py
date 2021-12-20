arg = input().split()
A = int(arg[0])
B = int(arg[1])
C = int(arg[2])

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
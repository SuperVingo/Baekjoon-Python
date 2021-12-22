arg = input().split()
A = int(arg[0])
B = int(arg[1])

if(A > B):
    print(">")
elif(A < B):
    print("<")
else:
    print("==")
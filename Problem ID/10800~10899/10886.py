n = int(input())
lst = [0, 0]
for i in range(n):
    lst[int(input())] += 1
if(lst[0] > lst[1]):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
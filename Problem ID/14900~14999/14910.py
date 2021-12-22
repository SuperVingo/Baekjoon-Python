n = input().split()
lst = [int(n[i]) for i in range(len(n))]
bef = sorted(lst)
if(lst == bef):
    print('Good')
else:
    print('Bad')
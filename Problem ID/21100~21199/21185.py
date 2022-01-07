a = int(input())
if(a % 4 == 1 or a % 4 == 3):
    print('Either')
elif(a % 4 == 2):
    print('Odd')
else:
    print('Even')
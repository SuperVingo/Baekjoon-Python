lst = input().split()
asc = ['1', '2', '3', '4', '5', '6', '7', '8']
des = asc[::-1]
if(lst == asc):
    print('ascending')
elif(lst == des):
    print('descending')
else:
    print('mixed')
user_input = input().split()
a = int(user_input[0])
b = int(user_input[1])
v = int(user_input[2])

t = int((v-b-1)/(a-b)+1)
print(t)
line = input().split()
y = int(line[0])
x = int(line[1])

board = []
for i in range(y):
    board.append(list(input()))

def getCostSW(part:list):
    swboard = [
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ]
    cnt = 0
    for i in range(8):
        for j in range(8):
            if(part[i][j] != swboard[i][j]):
                cnt += 1
    return cnt

def getCostSB(part:list):
    sbboard = [
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ]
    cnt = 0
    for i in range(8):
        for j in range(8):
            if(part[i][j] != sbboard[i][j]):
                cnt += 1
    return cnt

cost = 91
for sy in range(y-7):
    for sx in range(x-7):
        partial = []
        for _ in range(8):
            partial.append(board[sy+_][sx:sx+8])
        cost = min(cost, getCostSB(partial), getCostSW(partial))
print(cost)


import sys
input = sys.stdin.readline

global yee, answer

board = [list(input()) for _ in range(5)]
answer = 0
check = [[False] * 5 for _ in range(5)]
yee = []
dx = [1,0,-1,0]
dy = [0,-1,0,1]

def dfs(Y, level, loc):
    global yee, answer
    if level == 7:
        if Y >= 4:
            return
        answer += 1
        return
    else:
        if Y >= 4:
            return
        for i in range(4):
            x = loc[0] + dx[i]
            y = loc[1] + dy[i]
            if 0<=x<5 and 0<=y<5 and (check[x][y] == False):
                check[x][y] = True
                yee.append(board[x][y])
                if board[x][y] == 'Y':
                    dfs(Y + 1, level + 1, (x, y))
                else:
                    dfs(Y, level + 1, (x, y))
                yee.pop()
                check[x][y] = False
for i in range(5):
    for j in range(5):
        dfs(0,0,(i,j))

print(answer)
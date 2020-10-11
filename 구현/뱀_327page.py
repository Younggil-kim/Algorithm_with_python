#문제 해석
#뱀게임 규칙에 따라 구현하세여
#예외처리 꼭 생각할것.!
#통과
import sys

def snaketail(a,b):
    global snakeY
    global snakeX
    for i in reversed(range(len(snakeX)-1)):
        snakeX[i] = snakeX[i+1]
        snakeY[i] = snakeY[i+1]
    snakeX[-1] = a
    snakeY[-1] = b
    return

def isTail(a,b):
    global snakeY
    global snakeX
    for i in range(len(snakeX)):
        if a == snakeX[i] and b == snakeY[i]:
            return True
    return False

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apple = list()
for i in range(K):
    apple.append(list(map(int,sys.stdin.readline().split())))
L = int(sys.stdin.readline())
command = list()
for i in range(L):
    command.append(list(sys.stdin.readline().split()))


cnt = 0

snakeX = [1]#초기 위치, 사과를 먹으면 어펜드
snakeY = [1]

dir = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


lst = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(len(apple)):
    lst[apple[i][0]][apple[i][1]] = 1

i = 0

while True:
    cnt = cnt + 1
    lst[snakeX[-1]][snakeY[-1]] = 2
    nextSnakeX = snakeX[-1] + dx[dir]
    nextSnakeY = snakeY[-1] + dy[dir]#이동시에 전체에 + -를 해줘야할듯

    if i < L:
        if cnt == int(command[i][0]):
            if command[i][1] == 'D':
                dir = dir + 1
                if dir == 4:
                    dir = 0
            else:
                dir = dir - 1
                if dir == -1:
                    dir = 3
            i = i + 1

    if nextSnakeX < 1 or nextSnakeY < 1 or nextSnakeX > N or nextSnakeY > N or lst[nextSnakeX][nextSnakeY] == 2:#벽에 부딪히면
        print(cnt)
        break
    else:
        if lst[nextSnakeX][nextSnakeY] == 1:#사과가 있으면
            snakeX.append(nextSnakeX)
            snakeY.append(nextSnakeY)#길이 늘리기
            lst[nextSnakeX][nextSnakeY] = 2
        elif lst[nextSnakeX][nextSnakeY] == 0:#사과가 없으면
            snakeX.append(nextSnakeX)
            snakeY.append(nextSnakeY)
            a = snakeX.pop(0)
            b = snakeY.pop(0)
            lst[a][b] = 0

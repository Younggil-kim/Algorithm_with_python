#N*N의 시험관이 있다
# 바이러스가 한칸크기로 있는데, 상하좌우로 증식한다
# 여러 종류의 바이러스가 있다 1~K번까지 K가지가 있다.
# 위치 정보가 주어졌을 때, (x,y)에 존재하는 바이러스 종류를 찾아라

#생각
# 숫자 낮은거부터 큐에 집어넣으면 될듯?
# 단순 반복문으로 1부터 집어넣으려고하면 시간초과가 당연히 뜸
# 따라서, 리스트로 받아서 정렬 후 돌리던가하는 방법을 사용해야 함
# 나는 우선순위 큐를 사용해서 다시 큐에 집어넣었음

# 1초면 한번 돌리고 2초면 두번돌리고 해야함

from collections import deque
from queue import PriorityQueue

N, K = map(int, input().split())

lst = list()

for i in range(N):
    lst.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

que = deque()
que1 = PriorityQueue()
cnt = 0

for i in range(N):
    for j in range(N):
        if lst[i][j] != 0:
            que1.put((lst[i][j],(i, j, 0)))
            cnt = cnt + 1

for i in range(cnt):
    x, y, s = que1.get()[1]
    que.append((x,y,s))

def bfs():
    while que:
        x, y, s = que.popleft()
        if s == S:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if lst[nx][ny] == 0:
                lst[nx][ny] = lst[x][y]
                que.append((nx,ny, s+1))
    return True

bfs()
print(lst[X-1][Y-1])
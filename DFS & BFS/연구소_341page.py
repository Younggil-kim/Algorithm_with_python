#문제 해석
#바이러스가 상하좌우 인접한 빈칸으로 전부 퍼져나갈 수 있다
#바이러스는 2 퍼져나갈 공간은 0 벽은 1이다.
# 벽을 3개 세울 수 있는데, 아무 벽 세우지 않으면 바이러스는 모든 빈칸으로 퍼져나갈 수 있다.
# 안전영역 크기의 최대값을 구하라

# 연구소의 크기는 최대 8*8이므로, 64*65*63 전체 완전탐색으로 돌려도 될듯
# 그러면 어떻게 뽑을거야 벽을
# 0인 부분의 인덱스를 전부 받아와서, 리스트에 저장해 놓고, 리스트에서 3개 뽑아, 중복 안되게
# 그러면 itertool쓰고 3개 받아온 다음에, 벽 세우고 bfs나 dfs돌려서 최대값 구하면 될듯?
from itertools import combinations
from collections import deque
import copy
N, M = map(int,input().split())

grp = list()
for i in range(N):
    grp.append(list(map(int,input().split())))

grpCopy = copy.deepcopy(grp)
que = deque()

lst = list()
for i in range(N):
    for j in range(M):
        if grp[i][j] == 0:
            lst.append((i,j))

wall = list(combinations(lst,3))#3개 벽 가능한 경우의 수

result = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]
#bfs로 구현

def bfs():
    for i in range(N):
        for j in range(M):
            if grp[i][j] == 2:
                que.append((i,j))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if grp[nx][ny] == 1:
                continue
            if grp[nx][ny] == 0:
                grp[nx][ny] = 2
                que.append((nx,ny))
    return grp

#벽 세우고 bfs돌리고 다시 0으로 바꾸고
for i in wall:
    cnt = 0

    for j in range(3):
        x, y = i[j]
        grp[x][y] = 1#벽세우고

    b = bfs()#돌리고
    for k in b:
        a = k.count(0)
        cnt = cnt + a
    result.append(cnt)
    grp = copy.deepcopy(grpCopy)

print(max(result))
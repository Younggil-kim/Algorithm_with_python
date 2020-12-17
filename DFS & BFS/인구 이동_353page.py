#pypy3 통과 python 시초
from collections import deque

N, L, R = map(int, input().split())
grp = list()
for i in range(N):
    grp.append(list(map(int, input().split())))#그래프 받아오기

dx = [1,-1,0,0]
dy = [0,0,1,-1]
que = deque()

def bfs(a, b, count):
    #시작하는 나라의 인구수 합할게 필요함
    total = grp[a][b]
    unite = 1
    que.append((a,b))

    unite_lst = list()
    unite_lst.append((a,b))

    union[a][b] = count
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue#벗어나면 그냥 넘기고
            if L <= abs(grp[nx][ny] - grp[x][y]) <= R and union[nx][ny] == -1:#아직 방문처리 안되었고, 차이가 난다면
                total = total + grp[nx][ny]# 나라 인구 더해주고
                unite += 1 #나라 수를 1 올리고
                que.append((nx, ny))#큐에다 nx ny 넣어주기
                unite_lst.append((nx, ny))
                union[nx][ny] = count

    people = total//unite
    for i,j in unite_lst:
        grp[i][j] = people
    return True

total_cnt = 0
while True:
    union = [[-1 for k in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:#미방문처리면
                bfs(i,j,count)
                count += 1
    if count == N*N:
        break
    total_cnt += 1

print(total_cnt)
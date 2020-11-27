from collections import deque
test = int(input())


def bfs(x, y, n):
    result = [[INF for i in range(N)] for _ in range(N)]
    grp = deque()
    grp.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result[x][y] = lst[x][y]
    while grp:
        x, y = grp.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:  # 벽이거나 부딪히면 제외
                continue
            if result[nx][ny] <= result[x][y] + lst[nx][ny]:
                continue
            result[nx][ny] = min(result[x][y] + lst[nx][ny], result[nx][ny])
            grp.append((nx,ny))
    return result

INF = int(1e9)
for i in range(test):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int,input().split())))
    re = bfs(0,0,N)
    print(re[N-1][N-1])

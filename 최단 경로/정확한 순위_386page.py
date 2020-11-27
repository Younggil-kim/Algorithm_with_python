
N, M = map(int, input().split())
INF = int(1e9)

grp = [[INF]*(N+1) for i in range(N+1)]

for i in range(1,N+1):
    grp[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    grp[a][b] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            grp[i][j] = min(grp[i][j], grp[i][k] + grp[k][j])

result = 0
for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        if grp[i][j] != INF or grp[j][i] != INF:
            cnt = cnt + 1
    if cnt == N:
        result = result + 1

print(result)
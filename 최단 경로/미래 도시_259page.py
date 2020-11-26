N, M = map(int,input().split())
INF = int(1e9)
grp = [[INF]*(N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    grp[a][b] = 1
    grp[b][a] = 1
for i in range(1,N+1):
    grp[i][i] = 0

x, k = map(int, input().split())

for i in range(1,N+1):#플루이드 수행
    for j in range(1,N+1):
        for s in range(1,N+1):
            grp[j][s] = min(grp[j][s], grp[j][i] + grp[i][s])

result = grp[1][k] + grp[k][x]

if result >= INF:
    print(-1)
else:
    print(result)
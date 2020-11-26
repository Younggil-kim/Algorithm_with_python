import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = int(1e9)

grp = [[INF]*(N+1) for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < grp[a][b]:
        grp[a][b] = c
for i in range(1,N+1):
    grp[i][i] = 0


for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            grp[i][j] = min(grp[i][j], grp[i][k] + grp[k][j])

for i in range(1,N+1):
    for j in range(1, N+1):
        if grp[i][j] == INF:
            if j == N:
                print(0, end="")
            else:
                print(0,end=" ")
        else:
            if j == N:
                print(grp[i][j],end="")
            else:
                print(grp[i][j],end=" ")
    print(end="\n")
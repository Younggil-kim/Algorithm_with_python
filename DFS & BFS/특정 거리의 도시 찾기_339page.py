from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
grp = [[]*(N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    grp[a].append(b)

table = [-1]* (N+1)
que = deque()
table[X] = 0
que.append(X)

while que:
    cur = que.popleft()
    for i in grp[cur]:
        if table[i] == -1:#방문하지 않은 경우
            table[i] = table[cur] + 1
            que.append(i)

if table.count(K) == 0:
    print(-1)
else:
    table = [i for i in range(len(table)) if table[i] == K]
    print(*table)
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
grp = [[]for i in range(n+1)]

dis = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    grp[x].append((y,z))

def dijkstra(start):
    q = list()
    heapq.heappush(q, (0,start))
    dis[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in grp[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

cnt = 0
maximum = 0

for i in dis:
    if i != INF:
        cnt = cnt + 1
        maximum = max(maximum, i)

print(cnt-1, maximum)
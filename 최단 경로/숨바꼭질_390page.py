import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
start = 1
grp = [[]*(N+1) for i in range(N+1)]

table = [INF]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    grp[a].append((b,1))
    grp[b].append((a,1))

def dijkstra(start):
    lst = list()
    heapq.heappush(lst, (0, start))#비용, 1번노드 부터 시작
    table[start] = 0
    while lst:
        cost, fin = heapq.heappop(lst)
        if table[fin] < cost: #코스트가 더 크면
            continue#무시
        for i in grp[fin]:#아니면 거쳐서 갈거야
            trans = cost + i[1]
            if trans < table[i[0]]: #거쳐서가는게 더 작으면 최신화
                table[i[0]] = trans
                heapq.heappush(lst, (trans, i[0]))

dijkstra(start)

print(table)
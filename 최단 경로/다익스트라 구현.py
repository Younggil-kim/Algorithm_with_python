import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int,input().split())

start = int(input())

grp = [[] for i in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    grp[u].append((v,w))#3번에서 W비용으로 v로 갈 수 있음

table = [INF]*(V+1)

def dijkstra(start):
    lst = list()  # 힙
    heapq.heappush(lst, (0, start))#시작 하는 노드
    table[start] = 0#시작 부분의 비용은 0
    while lst:#힙이 다 빌때까지
        cost, fin = heapq.heappop(lst)#힙에서 하나 꺼내와서
        if table[fin] < cost:#코스트 테이블에서 이미 코스트보다 작으면
            continue#무시
        for i in grp[fin]:#그게 아닌경우 그래프에서 해당 경로를 통해 이동할 수 있는 가장 짧은 곳으로 감
            cst = cost + i[1]#거쳐서 이동하면 코스트에 그 가장 짧은 거리만큼이 더해짐
            if cst < table[i[0]]:#코스트가 더 짧은경우
                table[i[0]] = cst#코스트 테이블의 거쳐서 이동한 곳을 cst로 최신화
                heapq.heappush(lst, (cst, i[0]))#이후 힙에 집어 넣음

dijkstra(start)

for i in range(1,len(table)):
    if table[i] >= INF:
        table[i] = "INF"

for i in table[1:]:
    print(i)
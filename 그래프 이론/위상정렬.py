from collections import deque

v, e = map(int, input().split())

indegree = [0] *(v+1)

grp = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    grp[a].append(b)#A에서 B로 이동 가능
    indegree[b] += 1#진입 차수 1 증가

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)#진입차수 0인거 먼저 집어넣기

    while q:
        now = q.popleft()
        result.append(now)
        for i in grp[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()
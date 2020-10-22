#문제 해석
# 단방향 그래프가 존재 할 때, 최단거리인곳을 찾는 것
# bfs를 돌면서 갔던곳은 True체크 해주고, 마지막에 도달했을때 False라면 출력해주고
# False가 없으면 -1 출력

#pypy3아니면 시간초과 뜨는듯

#시간, 공간 복잡도 생각 잘하고 설계 해서 들어갈 것
from collections import deque

N, M, K, X = map(int, input().split())
grp = [[] for i in range(N+1)]

num = [-1]*(N+1)
num[X] = 0

for i in range(M):
    x, y = map(int, input().split())
    grp[x].append(y)#불필요한 정보까지 다 넣으면 메모리 초과 뜸

que = deque()

que.append(X)

while que:
    x = que.popleft()#처음 방문한 곳
    for i in grp[x]:
        if num[i] == -1:#이전에 방문하지 않은 경우에는
            num[i] = num[x] + 1# 넘값은 최신화
            que.append(i)#이후 방문

cnt = False
for i in range(N+1):#반복문 돌리면서 출력
    if num[i] == K:
        print(i)
        cnt = True
if cnt is False:
    print(-1)
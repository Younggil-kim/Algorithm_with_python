#문제  해석
#이차원 리스트가 주어지고 0과 1로 나누어져있다.
#0으로 연결된 조각의 개수를 세어라

#DFS로 간단하게 해결가능
# 0,0부터 돌면서 상하좌우 DFS돌려주면 됨
# 전부다 맞으면 트루 아니면 탈락
import sys

N, M = map(int,sys.stdin.readline().split())
lst = list()
for i in range(N):
    lst.append(list(map(int,input())))

result = 0
print(lst)
def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False#조건 벗어나면 아웃
    if lst[x][y] == 0:#노드 방문하지 않았으면
        lst[x][y] = 2 #노드 방문
        print(x,y)
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    else:
        return False

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            result = result + 1

print(result)
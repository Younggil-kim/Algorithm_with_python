#문제 해석

#벽을 3개 세워서 학생들이 선생님 시선에 구애받지 않도록 설치할수 있나 없나 판단하는 프로그램

#bfs를 상하, 좌우 두개를 만들어서 확인한다
#그러려면 데큐도 두개 있어야한다.

#벽을 3개 세우려면 조합을 사용한다.



from itertools import combinations
from collections import deque
import copy

N = int(input())
lst = list()
for i in range(N):
    lst.append(list(input().split()))

wall = list()
que = deque()
back = deque()

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'X':#빈 공간
            wall.append((i,j))
        elif lst[i][j] == 'T':
            que.append((i,j))# 선생님 시선

back = que.copy()
wall3 = list(combinations(wall, 3))# 벽 3개 조합


def teacher():
    while que:
        x, y = que.popleft()
        nx1 = x
        nx2 = x
        while True:
            nx1 = nx1 + 1
            if nx1 >= N:
                break
            if lst[nx1][y] == 'S':
                return True
            if lst[nx1][y] == 'W':
                break
        while True:
            nx1 = nx2 - 1
            if nx2 < 0:
                break
            if lst[nx1][y] == 'S':
                return True
            elif lst[nx1][y] == 'W':
                break
        ny1 = y
        ny2 = y
        while True:
            ny1 = ny1 + 1
            if ny1 >= N:
                break
            if lst[x][ny1] == 'S':
                return True
            elif lst[x][ny1] == 'W':
                break
        while True:
            ny2 = ny2 -1
            if ny2 < 0:
                break
            if lst[x][ny2] == 'S':
                return True
            elif lst[x][ny2] == 'W':
                break

plg = False
for i in wall3:
    for j in i:
        x, y = j
        lst[x][y] = 'W'
    if teacher() is True:
        plg = True
    que = back.copy()
    for j in i:
        x, y = j
        lst[x][y] = 'X'

if plg is False:
    print("YES")
else:
    print("NO")

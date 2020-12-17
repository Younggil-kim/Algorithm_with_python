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

copy_lst = copy.deepcopy(lst)

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'X':#빈 공간
            wall.append((i,j))
        elif lst[i][j] == 'T':
            que.append((i,j))# 선생님 시선
copy_que = copy.deepcopy(que)

wall3 = list(combinations(wall, 3))# 벽 3개 조합

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            copyx = x
            copyy = y
            while True:
                nx = copyx + dx[i]
                ny = copyy + dy[i]
                if nx >= N or ny >= N or nx < 0 or ny < 0:
                    break
                if lst[nx][ny] == 'O':#벽이면 노진행
                    break
                if lst[nx][ny] == 'S':#학생이면
                    return False
                if lst[nx][ny] == 'X' or lst[nx][ny] == 'T':#X,T면 진행
                    lst[nx][ny] = 'T'#선생 시선으로 바꾸고
                    copyx = nx
                    copyy = ny
    return True
#벽 3개 세우고, bfs 돌리고, 벽 3개 지우고 반복

is_teacher = False
while wall3:
    first, second, third = wall3.pop()
    lst[first[0]][first[1]] = 'O'
    lst[second[0]][second[1]] = 'O'
    lst[third[0]][third[1]] = 'O'
    a = bfs()
    if a:#학생이 걸리지 않았으면
        is_teacher = True
        break
    else:#걸렸으면 초기화 후 다시 벽 세우기
        que = copy.deepcopy(copy_que)
        lst = copy.deepcopy(copy_lst)


if is_teacher:
    print("YES")
else:
    print("NO")
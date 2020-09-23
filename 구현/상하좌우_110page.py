#문제 해석
# N*N의 지도가 있고, 맨왼쪽 위 1,1 젤 오른쪽 아래 N,N이다
# 여기서 상하좌우 명령이 들어오면 1,1에서 시작해서 여행자가 어디에 마지막으로 위치할지 출력하라
# 단 인덱스를 벗어나는 경우의 명령은 무시한다

# 생각
# 함수로 구현하면 될 거같은데?
# 명령을 받아오고, 그 명령이고 인덱스 안벗어나면 이동

import sys

N = int(sys.stdin.readline())
lst = list(sys.stdin.readline().split())

position = [1,1]
def moving(com ,site):
    if com == 'L':
        if site[1] - 1 != 0:
            site[1] = site[1] - 1
    elif com == 'R':
        if site[1] + 1 != N+1:
            site[1] = site[1] + 1
    elif com == 'U':
        if site[0] - 1 != 0:
            site[0] = site[0] - 1
    elif com == 'D':
        if site[0] + 1 != N+1:
            site[0] = site[0] + 1

for i in lst:
    moving(i,position)

print(position[0],position[1])
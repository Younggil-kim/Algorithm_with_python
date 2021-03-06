#문제 해석 시작시간 PM 6 56
# 캐릭터가 있는 장소는 N*N 사각형 내의 한 장소
# 각 칸은 육지 또는 바다
# 캐릭터는 동서남북중 한곳을 바라봄
# 맵의 각 칸은 (A,B)이고 A는 북으로부터 떨어진 칸 개수
#B는 서쪽으로부터 떨어진 개수이다
# 캐릭터는 상하좌우로 움직일 수 있고 바다는 갈 수 없다
# 1 현재 위치에서 현재방향 기준으로 왼쪽방향부터 차례로 갈 곳 선정
# 2 캐릭터 바로 왼쪽에 가보지 않은 칸이 있으면 왼쪽으로 회전한고, 왼쪽으로 한칸 전진
# 3. 만약 네 방향 모두 이미 가 본 방향이거나, 바다로 되어 있는 경우, 바라보는 방향을 유지한채로 한칸 뒤로가고, 1단계로 돌아간다
# 뒤쪽이 바다인 경우에는 운직임을 멈춘다.

# 캐릭터를 이동시킨 후에 방문한 칸의 수를 출력하는 프로그램을 작성하라.

#첫 줄에 N*M을 공백으로 구분
# 둘째줄에 캐릭터가 있는 곳의 좌표와 바라보는 방향이 구분됨
#셋째 줄 부터 육지인지 바다인지 입력한다.
# 0은 육지 1ㅇ은 바다
# 캐릭터 시작 위치는 모두 육지이다

#보는 방향에 따른 포지션의 위치를 리스트로 설정해 놓는다.
#방향을 받아오고,  0 북, 1 동 2 남 3 서 니까
#보는 방향이 북서남동 이런식으로 계속 움직이는 형태 그러면 결국 처음 보는 방향에서
# 왼쪽으로 돌아서 바단지 아닌지, 갔던곳인지 아닌지 검사 후, 둘다 아니면 전진
# 이런 문제는 방향벡터를 쓰는게 좋아/

N, M = map(int, input().split())
X, Y, sight = map(int,input().split())
lst = list()
for i in range(N):
    lst.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
def turn_left():
    global sight
    sight = sight -1
    if sight == -1:
        sight = 3

def is_all_close(X,Y):
    global lst
    if lst[X+1][Y] != 0 and lst[X-1][Y] != 0 and lst[X][Y+1] != 0 and lst[X][Y-1] != 0:
        return True

while True:
    turn_left()#왼쪽으로 돌아

    if lst[X + dx[sight]][Y + dy[sight]] == 0:# 그 왼쪽앞에있는게 육지임?
        X = X + dx[sight]
        Y = Y + dy[sight]
        lst[X][Y] = 2#그렇다면 전진
        cnt = cnt + 1
    else:
        if is_all_close(X,Y) is True:# 4면이 다 닫혀있으면 방향그대로 후진해야해
            if lst[X - dx[sight]][Y - dy[sight]] == 1:#근데 그 뒤가 바다면 종료
                print(cnt)
                break
            else:#4면이 닫혀있는데, 그 뒤가 바다가 아니면
                X = X - dx[sight]
                Y = Y - dy[sight]


#문제 이해하기가 좀 어려웠던거 같다.
#아직 뇌지컬이 딸린다. 방향벡터를 이용하는것 잘 기억해두도록 하자.
#캐릭터 이동하고 이런문제는 방향벡터 이용하면 되게 편하다.

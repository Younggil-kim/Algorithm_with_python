#시작 시간 PM 11:50
#종료 시간 AM 12:05
#문제 해석
'''한 마을에 모험가가 N명 있다, N명 모험가를 대상으로, 공포도를 측정했는데, 공포도가 높으면 위험 상황에서 대처하지 못함
길드장은 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 참여해야 여행을 갈 수 있다.
최대 몇개의 그룹이 만들어 질 수 있는가'''

# 입력은 첫줄에 모험가 수 N, 둘째줄에 각 모험가의 공포도를 줌

#생각
#정렬을 한 뒤, 첫번째 모험가부터 N에서 공포도를 빼 주고, N이 맞춰지면 그대로 끝내고, N이 안맞춰지면 그 그룹대로 출발
# 가장 공포도가 큰 모험가부터, 크기에 맞게 빼 주고,
# 그 다음 모험가를 하는 순서
import sys
def pop_adventure(f):
    global lst
    for i in range(f):
        lst.pop()
    return

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()#정렬
cnt = 0

max_fear = lst[-1]# 가장 높은 공포도 가진 모험가를
while True:
    pop_adventure(max_fear)#정렬된 끝에서부터 (max_fear)명 뽑아감
    cnt = cnt + 1# 팀을 증가시킴
    if len(lst) == 0:# 만약 모험가가 비어있으면
        print(cnt)# 팀 개수 출력
        break
    else:#모험가가 남아있으면
        max_fear = lst[-1]#멕스 모험가 증가
#시작 시간 PM 11:50
#종료 시간 AM 12:05
#문제 해석
'''한 마을에 모험가가 N명 있다, N명 모험가를 대상으로, 공포도를 측정했는데, 공포도가 높으면 위험 상황에서 대처하지 못함
길드장은 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 참여해야 여행을 갈 수 있다.
최대 몇개의 그룹이 만들어 질 수 있는가'''

# 입력은 첫줄에 모험가 수 N, 둘째줄에 각 모험가의 공포도를 줌

#생각
#정렬을 한 뒤, 가장 공포도가 낮은 모험가부터 팀을 만드는데,
#지금 추가하는 공포도가 팀 숫자보다 크면 팀 결성,
import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
team = list()
lst.sort()#정렬
cnt = 0

for i in lst:
    team.append(i)#팀에 추가 시키고
    if i <= len(team):#지금 추가한 공포도가, 모험가 숫자보다 작거나 같으면
        cnt = cnt + 1# 팀 만듦
        del team[:]#현재 팀 초기화
print(cnt)

#문제 해석
# 가장 인접한 두 공유기 사이의 거리가 최대가 되도록 공유기를 놓아라

#생각
# [ 최소거리, 최대거리]를 기준으로 가운데를 mid로 잡는다
# 첫번째부터 순차적으로 놓을건데, 값 + mid의 값이 넘어가면 카운트를 올려주고
# 개수가 넘어가면 저장하고,
# 개수가 안되면 갭을 늘려준다.

#포인트는 최대거리와 최소거리의 중간값으로 조절하면서 좁혀나가야하는것


import sys

N, C = map(int, sys.stdin.readline().split())
lst = list()
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()

min_dtc = lst[1] - lst[0]#최소 갭
max_dtc = lst[-1] - lst[0]#최대 갭
result = 0

def binary_search(lst, target, start, end):
    global result
    while start <= end:
        val = lst[0]#첫번째 집 부터의 거리를 체크하기 위함
        cnt = 1#공유기 개수를 세기 위함
        mid = (start + end) //2#최소, 최대 갭의 중간
        for i in range(1,N):
            if lst[i] >= mid + val:#만약 첫번째 집부터 중간거리의 크기보다 집이 멀리있으면
                cnt = cnt + 1# 공유기 설치해주고
                val = lst[i]# 첫번째 집에서 설치하는 집으로 val을 바꾼다
        if cnt >= target:# 만약에 공유기가 타겟보다 많이 설치되었거나, 같다면
            start = mid + 1# 스타트를 올려줘서, 중간거리의 값을 올려준다
            result = mid # 갭이 점점 커지면서 최신화되는 거리의 값이 ㅈ정답
        else:# 만약 공유기가 타겟보다 설치되지 않았으면
            end = mid - 1#엔드를 줄여서, 중간거리의 값을 낮춰준다.
    return result

print(binary_search(lst, C, min_dtc, max_dtc))
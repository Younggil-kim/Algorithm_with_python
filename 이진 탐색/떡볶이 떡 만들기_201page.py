#문제 해석

#떡을 절단기로 자르고, 그 위에 남은 부분을 가져가는데
#요청한 길이가 M일때, 적어도 M만큼을 얻기 위해 절단기에 설정 할 높이의 최대값을 구하라

# 바이너리 서치로, 큰길이를 엔드 0을 시작점
# 그 중간을 중간값으로 만들고, 잘린 길이가 긴 경우
# 스타트를 올려준다,
# 계속 올리다가 작은 지점이 오면 전꺼 중간값 나타내주고 끝낸다

import sys
N, M = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

def binary_search(lst, target, start, end):
    global cut
    while start <= end:
        result = 0
        mid = (start + end)//2#이거로 인해 잘렸을때 계산
        for i in lst:
            if i > mid:
                result = result + (i-mid)
        if result < target: # 떡 길이가 부족하면
            end = mid-1
        else: #떡 길이가 알맞거나 큰 경우
            cut = mid#최신화 시켜주고
            start = mid + 1# 스타트를 올려준다

binary_search(lst, M, 0, max(lst))
print(cut)
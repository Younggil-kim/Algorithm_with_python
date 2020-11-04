#문제 해석

#인덱스를 접근하고, 인덱스와 값이 일치하면 출력해주고
#인덱스보다 값이 작으면 (인덱스가 3인데 값이 2이면 end 줄이기
#인덱스보다 값이 크면 (인덱스가 3인데 값이 4이면 start 높이기
#이렇게해서 일치하면 출력해주면 될듯

import sys
cnt = 0
def binary_search(lst, start, end):
    global cnt
    while start <= end:
        mid = (start + end)//2

        if lst[mid] == mid:
            cnt = cnt + 1
            print(mid)
            return
        elif lst[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
binary_search(lst, 0, N-1)
if cnt == 0:
    print(-1)
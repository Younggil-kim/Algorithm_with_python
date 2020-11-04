#첫번째 풀이 bisect이용
from bisect import bisect_left, bisect_right
import sys

N, x = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

def range_num(lst, start, end):
    a = bisect_left(lst, start)
    b = bisect_right(lst, end)
    return b - a

cnt = range_num(lst, x, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)

#두번째 풀이 두번의 이진탐색 이용

import sys

def binary_search_left(lst, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if lst[mid] == target:
            end = mid
            if end == 0 or lst[end -1] != target:
                return end
        elif lst[mid] > target:# 타겟보다 mid값이 더 크면
            end = mid - 1
        else:
            start = mid + 1
    return None

def binary_search_right(lst, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if lst[mid] == target:
            start = mid
            if start == N-1 or lst[start +1] != target:
                return start
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N, x = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

a = binary_search_left(lst, x, 0,N-1)
b = binary_search_right(lst, x, 0,N-1)

if a is None or b is None:
    print(-1)
else:
    print(b-a+1)
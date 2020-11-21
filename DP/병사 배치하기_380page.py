from bisect import bisect_left

N = int(input())
lst = list(map(int, input().split()))
lst.reverse()
result = list()
cnt = 0
for i in lst:
    num = bisect_left(result, i)
    if num < len(result):#왼쪽에 들어가야하면
        result[num] = i
        cnt = cnt + 1
    else:
        result.append(i)

print(cnt)
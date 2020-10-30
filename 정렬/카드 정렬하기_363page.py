#문제 해석

#카드 개수가 적은 순서대로 그냥 쭉 풀면될거같은데?

import heapq

N = int(input())
lst = list()
for i in range(N):
    heapq.heappush(lst, int(input()))
result = 0
while True:
    if len(lst) == 1:
        print(result)
        break
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    c = a + b
    result = result + c
    heapq.heappush(lst, c)


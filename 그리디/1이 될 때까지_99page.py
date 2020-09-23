#문제 해석
# N이 1이 될 때 까지 두과정 중 하나를 반복 선택하려 함
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다
# 나누는 연산은 나누어떨어질 때만 사용가능하다.
# 첫째줄에 N과 K가 주어질때, 최소 연산을 구하라

#생각
# K배수가 되면 K로 나누고 아니면 1을 계속 빼주면 됨 그냥 단순히

#가장 단순하게 푼 방법
# import sys
#
# N, K = map(int, sys.stdin.readline().split())
# cnt = 0
# while True:
#     if N == 1:
#         print(cnt)
#         break
#     else:
#         if N % K == 0:
#             N = N/K
#             cnt = cnt + 1
#         else:
#             N = N -1
#             cnt = cnt + 1

# 조금 효율적으로 동작하기 위해, 빼는 과정을 한번에 하는 코드
# 1씩 계속 반복하는것보다, 나머지를 구해서 나머지를 한번에 뺴는게 효율적

import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
while True:
    if N == 1:
        print(cnt)
        break
    elif N == 0:
        print(cnt-1)
        break
    else:
        if N % K != 0:
            cnt = cnt + (N % K)
            N = N - ( N % K )
        else:
            N = int(N / K)
            cnt = cnt + 1

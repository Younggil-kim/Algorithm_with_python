#문제 해석
#N * M의 형태로 놓여있다
# N은 행, M은 열의 개수를 의미
# 뽑고자 하는 카드가 포함된 행을 선택
# 잏 ㅜ선택된 행에 포함된 카드 중 가장 낮은 카드 뽑기
# 처음에 카드를 골라낼 행 선택 할 때, 이후에 해당 행에서 가장 낮은 카드를 뽑을것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

# 쉽게 설명해서 2차원 리스트가 있는데 각 행에서 가장 낮은수를 뽑은 후, 그 중에서 가장 큰 수를 출력하란 소리

# 첫줄에는 N과 M이 주어지고
# 둘째줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어짐

# 간단한거같은데, min으로 선택한 다음, max로 출력해주면 될거같은데

import sys

N, M = map(int, sys.stdin.readline().split())
lst = list()
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

maximum = 0
for i in range(N):
    if min(lst[i]) > maximum:
        maximum = min(lst[i])
print(maximum)

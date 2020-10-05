#문제 해석
#무게가 다른 볼링공의 조합의 개수를 맞추는 문제

#생각
#1 3 2 3 2가 있는 경우
# 1을 빼면 4가지 경우
# 1,2를 빼면 2가지경우*2 2의 개수

#1 5 4 3 2 4 5 2의 경우
#1을 빼면 7가지 경우
#1,2를 빼면 5가지경우 *2(2의 개수)17
#1,2,3을 빼면 4가지 경우21
#1,2,3,4를 뺴면 2 * 2 25

#결국에 1부터 M까지 반복문을 돌면서 개수 체크해주고,
# 뺀수 * 개수를 곱해주면 됨

import sys

N, M = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
cnt = 0
def list_remove(x):
    global lst
    for i in range(lst.count(x)):
        lst.remove(x)
    return

for i in range(1,M):
    cnt = cnt + lst.count(i)*(len(lst)-lst.count(i))
    list_remove(i)

print(cnt)
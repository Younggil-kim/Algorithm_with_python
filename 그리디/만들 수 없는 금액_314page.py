#문제 해석 시작시간 : AP 2:45
#N개의 동전을 가지고 있을 때, 이 동전들로 만들수 없는 가장 최소 금액을 판단하라



import itertools
import sys

N = int(sys.stdin.readline())
coin = list(map(int,sys.stdin.readline().split()))
lst = set()
for i in range(1,N+1):
    x = itertools.combinations(coin,i)
    for i in x:
        lst.add(sum(i))

check = 1
while True:
    if check not in lst:
        print(check)
        break
    else:
        check = check + 1

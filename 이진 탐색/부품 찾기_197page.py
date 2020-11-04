#문제 해석

#부품이 N개 있고, 부품은 각 정수의 고유 번호가 있다.
# M개의 부품을 대량구매하겠다며 견적을 요청했고, M개 종류 모두 확인해서 견적을 짜야한다.
# 가게 안에 부품이 모두 있는지 확인하는 프로그램을 짜라

# 정렬후 바이너리 서치를 통해서, 바로바로 찾는다
import sys

def binary_search(lst, target, start, end):
    if start > end:
        print("no",end=" ")
        return
    else:
        mid = (start + end)//2
        if lst[mid] == target:
            print("yes",end=" ")
            return
        elif lst[mid] > target:
            return binary_search(lst,target, start, mid-1)
        else:
            return binary_search(lst,target,mid+1, end)

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
tgt = list(map(int,sys.stdin.readline().split()))

for i in tgt:
    binary_search(lst, i, 0, N-1)
#문제 해석

#중간값을 찾아라

N = int(input())

lst = list(map(int,input().split()))

lst.sort()

print(lst[(N-1)//2 ])

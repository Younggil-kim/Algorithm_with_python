# import sys
#
# #크루스칼은 기본적으로 ElogE 근데 이게 10만이라 메모리 초과가 남
# #따라서 간선하나하나 전부 확인하는것은문제가 있음.
#
# input = sys.stdin.readline
#
# #특정 원소가 속해있는 루트노드 찾기
# def find_parent(parent, x):
#     #만약 루트노드 아니면 재귀로 계속해서 루트찾기
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# #두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# def distince(a,b):
#     cost = min(abs(a[0]-b[0]),abs(a[1]-b[1]),abs(a[2]-b[2]))
#     return cost
#
# V= int(input())#노드, 간선 개수 받아오기
# parent = [0] * (V+1)#부모 테이블
#
# edges = []
# result = 0
#
# for i in range(1,V+1):
#     parent[i] = i
#
# sum_cost = 0
# lst = list()
# for _ in range(V):
#     a, b, c = map(int, input().split())
#     lst.append((a,b,c))
#
# for i in range(V-1):
#     for j in range(i+1,V):
#         cost = distince(lst[i],lst[j])
#         edges.append((cost, i, j))
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent,a) != find_parent(parent,b):
#         union_parent(parent,a,b)
#         result += cost
#
# print(result)


import sys

#크루스칼은 기본적으로 ElogE 근데 이게 10만이라 메모리 초과가 남
#따라서 간선하나하나 전부 확인하는것은문제가 있음.

input = sys.stdin.readline

#특정 원소가 속해있는 루트노드 찾기
def find_parent(parent, x):
    #만약 루트노드 아니면 재귀로 계속해서 루트찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



V= int(input())#노드, 간선 개수 받아오기
parent = [0] * (V+1)#부모 테이블

edges = []
result = 0

for i in range(1,V+1):
    parent[i] = i

sum_cost = 0
x = []
y = []
z = []
for _ in range(1,V+1):
    a, b, c = map(int, input().split())
    x.append((a,_))
    y.append((b,_))
    z.append((c,_))

x.sort()
y.sort()
z.sort()

for i in range(V-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1],x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1],y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1],z[i+1][1]))


edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
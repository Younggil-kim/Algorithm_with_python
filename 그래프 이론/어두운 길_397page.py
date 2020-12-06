import sys

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
V, E = map(int, input().split())#노드, 간선 개수 받아오기
parent = [0] * (V+1)#부모 테이블

edges = []
result = 0

for i in range(1,V+1):
    parent[i] = i

sum_cost = 0
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    sum_cost += cost
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(sum_cost- result)
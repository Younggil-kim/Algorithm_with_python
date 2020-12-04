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

#테이블의 각 노드의 부모를 자기자신으로 초기화
for i in range(1,V+1):
    parent[i] = i

cycle = False

for i in range(E):
    a, b = map(int, input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
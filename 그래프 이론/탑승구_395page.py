import sys
input = sys.stdin.readline


gate = int(input())
airplane = int(input())

grp = [0]*(gate+1)
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

for i in range(gate+1):#자기 자신으로 초기화
    grp[i] = i

cnt = 0

for i in range(airplane):
    a = int(input())
    dok = find_parent(grp, a)
    if dok != 0:
        union_parent(grp, a, dok-1)
        cnt = cnt + 1
    else:
        break
print(cnt)


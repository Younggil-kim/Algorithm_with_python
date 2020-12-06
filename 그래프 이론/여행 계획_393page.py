
def find_parent(parent, x):
    # 만약 루트노드 아니면 재귀로 계속해서 루트찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N, E = map(int, input().split())

lst = list()

for i in range(N):
    lst.append(list(map(int, input().split())))

parent = [0] * (N+1)#부모 테이블

for i in range(1,N+1):
    parent[i] = i

for i in range(1,N+1):
    for j in range(1, N+1):
        if lst[i-1][j-1] == 1:
            union_parent(parent,i,j)

result = list(map(int, input().split()))
travel = set()
for i in result:
    travel.add(find_parent(parent, i))

if len(travel) == 1:
    print("YES")
else:
    print("NO")


print(parent)
from collections import deque

test_case = int(input())

for i in range(test_case):
    v = int(input())
    lst = list(map(int, input().split()))#그래프
    result = []

    indegree = [0] * (v+1)#차수

    incrt = False

    grp = [[] for i in range(v+1)]

    #5에서 리스트 쭉
    for i in range(len(lst)):
        for j in lst[i+1:]:
            grp[lst[i]].append(j)
    m = int(input())

    for i in range(m):
        a, b = map(int, input().split())
        if b in grp[a]:
            grp[a].remove(b)
            grp[b].append(a)
        else:
            grp[b].remove(a)
            grp[a].append(b)

    for i in grp:
        for j in i:
            indegree[j] += 1

    que = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            que.append(i)

    only_one = True
    is_cycle = False

    for i in range(v):
        if len(que) == 0:
            is_cycle = True
            break
        if len(que) >= 2:
            only_one = False
            break
        now = que.popleft()
        result.append(now)

        for i in grp[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                que.append(i)

    if is_cycle:
        print("IMPOSSIBLE")
    elif not only_one:
        print("?")
    else:
        print(*result)

# def topology_sort():
#     que = deque()
#     for i in range(1, v + 1):
#         if indegree[i] == 0:
#             que.append(i)
#
#     if len(que) == 0:
#         print("IMPOSSIBLE")
#         return False
#     while que:
#         if len(que) >= 2:
#             print("?")
#             return False
#         now = que.popleft()
#         result.append(now)
#         cnt = 0
#         for i in grp[now]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 que.append(i)
#                 cnt += 1
#     return result

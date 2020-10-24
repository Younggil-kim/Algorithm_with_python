#문제 해석
# 연산자 끼워넣기
# 수와 수 사이에 연산자를 넣어서 수식을 만들 수 있다.
# 이 떄 주어진 수의 순서를 바꾸지 말고, 연산자를 끼워넣어 최소값과 최대값을 구하라

#생각
#dfs 재귀를 통해서 숫자 하나씩 빼면서 돌리고 결과 넣으면 될 듯

#재귀 사용시 리스트 pop을 해버리면 리스트 자체가 없어져버리니까 조심해야 함
#따라서, 이런 류에서는 리스트 pop이 아닌 인덱스 형태로 접근하는게 좋아보임



N = int(input())

lst = list(map(int,input().split()))
a,b,c,d = map(int,input().split())

result = list()

first = lst.pop(0)
def dfs(a,b,c,d, first, next):
    global lst
    global result
    if a == 0 and b == 0 and c == 0 and d == 0:
        result.append(first)
        return
    else:
        if a != 0:
            dfs(a-1,b,c,d,first + lst[next], next+1)
        if b != 0:
            dfs(a,b-1,c,d,first - lst[next], next+1)
        if c != 0:
            dfs(a,b,c-1,d, first * lst[next], next+1)
        if d != 0:
            dfs(a,b,c,d-1,int(first / lst[next]), next+1)

dfs(a,b,c,d,first,0)
print(max(result))
print(min(result))
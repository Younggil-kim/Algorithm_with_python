#문제 해석

#정렬 조건에 맞게 정렬하라
# 1. 국어 점수가 감소하는 순서로(내림차순 reverse)
# 2. 국어 점수가 같으면 영어 점수가 증가하는(오름차순)
# 3. 국 영 점수가 같으면 수학 점수가 감소하는 순서로(내림차순 reverse)
# 4. 모든 점수가 같으면 이름이 사전순으로

N = int(input())

lst = list()
for i in range(N):
    a, b, c, d = input().split()
    lst.append([a,int(b),int(c),int(d)])


lst.sort(key= lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(lst[i][0])
#문제 해석

#학생과 점수로 데이터가 주어지면, 성적 낮은 순으로 학생이름 출력하라

N = int(input())
lst = list()

for i in range(N):
    x, y = input().split()
    lst.append([x,int(y)])

lst.sort(key=lambda x: x[1])

for i in range(N):
    print(lst[i][0],end=" ")
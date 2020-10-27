#문제 해석

#입력된 수열을 큰수부터 작은수 내림차순으로 정렬하는 프로그램을 만드시오

N = int(input())
lst = list()
for i in range(3):
    lst.append(int(input()))

lst.sort(reverse=True)

print(*lst,end=" ")
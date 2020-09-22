#제한시간 30분, 시작시간 PM 8:16
# 문제 해석
# 다양한 수로 이루어진 배열이 있을때 수를 M번 더해 가장 큰 수를 만드는 것
# 단 해당하는 수가 연속으로 K번 만큼 더해질 수 없는것이 특징
# 첫줄에 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력

#생각
# 가장 큰 값이 두개 이상일 경우 그 수만 계속 더하는게 가능함
# 아닌 경우에는 큰값 3, 그 다음 값 1씩 계속 더해야 해

import sys

N, M, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

plg = 0
result = 0

X = lst.pop(lst.index(max(lst)))
print(lst)
if X in lst:
    result = X*M
else:
    for i in range(M):
        if plg == 3:
            result = result + max(lst)
            plg = 0
        else:
            result = result + X
            plg = plg + 1

print(result)

#종료 시간 PM 8:35
#걸린 시간 19분

#10분이면 풀 수 있는 문젠데, 반복문의 M을 N으로 잘못적고 한참 찾아다녔다.
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
        if plg == K:
            result = result + max(lst)
            plg = 0
        else:
            result = result + X
            plg = plg + 1

print(result)

#종료 시간 PM 8:35
#걸린 시간 19분

#10분이면 풀 수 있는 문젠데, 반복문의 M을 N으로 잘못적고 한참 찾아다녔다.

#더 효율적으로 계산 할 수 있는 방법은
#문제의 특성을 파악하는 것이다.

#가장 큰 수가 반복되는 횟수는(M //(k + 1)) * k 번이다
#예를 들어 M이 8 K가 3, 가장 큰 수가 6 두번째 큰 수가 5인 경우
# 6 6 6 5, 6 6 6 5 이런식으로 더해진다
# 이 경우는 M이 K+1로 나눠떨여져서 가능한데, 이후에 남는 수열도 생각해 줘야한다.
# 결국 가장 큰 값이 더해지는 횟수 count = M//(k+1) * k 에다가, M%(k+1)을 더해주는 값이다.
# 이후에 M번 - count * 두번째로 큰 값과, count * 가장 큰 값을 해주면 정답이 나온다.
# 코드는 내일 다시 짜보자.
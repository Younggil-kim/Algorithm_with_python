#문제 해석
#정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성


#간단하게 3중 for문으로도 할 수 있다.

N = int(input())
cnt = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt = cnt + 1
print(cnt)
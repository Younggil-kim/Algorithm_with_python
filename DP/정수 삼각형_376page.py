
N = int(input())
lst = list()
for i in range(N):
    lst.append(list(map(int, input().split())))

dp = [[0 for i in range(N)] for _ in range(N)]
dp[0][0] =lst[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + lst[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + lst[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + lst[i][j],dp[i-1][j-1] + lst[i][j])
print(max(dp[N-1]))
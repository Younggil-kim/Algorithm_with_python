N, M = map(int, input().split())
lst = list()
for i in range(N):
    lst.append(int(input()))

dp = [20000]*(M+1)

for i in lst:
    if i <= M:
        dp[i] = 1

for i in range(M+1):
    for j in lst:
        if j <= M and i-j >=0:
            dp[i] = min(dp[i], dp[i-j]+1)

if dp[M] == 20000:
    print(-1)
else:
    print(dp[M])
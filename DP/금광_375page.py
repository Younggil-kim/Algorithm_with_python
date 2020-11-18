case = int(input())

for n in range(case):
    N, M = map(int, input().split())
    lst = list(map(int,input().split()))
    grp = [[0 for _ in range(M)]for e in range(N) ]
    s = 0
    for j in range(N):
        for k in range(M):
            grp[j][k] = lst[s]
            s += 1

    dp = [[0 for _ in range(M)]for e in range(N)]
    for j in range(N):
        dp[j][0] = grp[j][0]

    for j in range(1,M):
        for i in range(N):
            if i == 0:
                dp[i][j] = max(dp[i][j-1] + grp[i][j], dp[i+1][j-1] + grp[i][j])
            elif i == N-1:
                dp[i][j] = max(dp[i][j-1] + grp[i][j], dp[i-1][j-1] + grp[i][j])
            else:
                dp[i][j] = max(dp[i][j - 1] + grp[i][j], dp[i - 1][j - 1] + grp[i][j], dp[i+1][j-1] + grp[i][j])

    maximum = 0
    for i in range(N):
        maximum = max(maximum, dp[i][M-1])
    print(maximum)
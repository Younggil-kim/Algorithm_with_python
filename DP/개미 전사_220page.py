#생각

N = int(input())
lst = list(map(int, input().split()))

dp = [0]*100# 인덱스의 방을 털었다가 아닌 인덱스 방까지 왔을때, 제일 많이 턴 경우가 저장되는 곳

dp[0] = lst[0]#첫번째꺼 털었고
dp[1] = max(lst[0], lst[1])# 두 번째것을 가지고 갈지, 아니면 두번째꺼 안하더라고 첫번째거를 들고 갈 지
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + lst[i])#
print(dp[N-1])
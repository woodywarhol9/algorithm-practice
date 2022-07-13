n = int(input())

# 각 자리수에서의 경우의 수를 저장
dp = [[0] * 10 for _ in range(n + 1)]
# 첫번째 자리 수는 0이 올 수 없기 때문에 0을 제외하고 1로 초기화
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        # 0일 떄는 앞 자리수가 1인 경우만 가능함
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        # 9일 떄는 앞 자리수가 8인 경우만 가능함
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(int(sum(dp[n]) % 1000000000))
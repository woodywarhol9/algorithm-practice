n = int(input())

dp = [0] * 1000001

for i in range(2, n + 1):
    a, b = 1e9, 1e9
    if i % 2 == 0:
        a = dp[i // 2] + 1
    if i % 3 == 0:
        b = dp[i // 3] + 1
    c = dp[i - 1] + 1
    dp[i] = min(a, b, c)

print(dp[n])
n = int(input())
num_list = [int(input()) for _ in range(n)]

dp = [0] * 300
dp[0] = num_list[0]

if n == 1:
    print(dp[0])
    exit(0)
dp[1] = num_list[0] + num_list[1]
if n == 2:
    print(dp[1])
    exit(0)
dp[2] = num_list[2] + max(num_list[0], num_list[1])

for i in range(3, n):
    dp[i] += max(num_list[i] + num_list[i - 1] + dp[i - 3], num_list[i] + dp[i - 2])
    
print(dp[n - 1])
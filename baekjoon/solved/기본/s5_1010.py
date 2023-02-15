"""
mCn을 구하는 문제.
파스칼 삼각형 이용.
"""

T = int(input())

dp = [[] for _ in range(30)]

for i in range(30):
    for j in range(i + 1):
        if j == 0 or j == i :
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])

for _ in range(T):
    n, m = map(int, input().split())
    print(dp[m][n])
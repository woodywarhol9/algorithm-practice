"""
정수 삼각형 : 금광 문제와 완전 동일한 문제.
"""

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n): # 층 선택
    for j in range(i + 1): # 원소 선택
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 오른쪽 위에서 내려오는 경우
        if j == i:
            up_right = 0
        else:
            up_right = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up_right)

# 마지막 층에서 최댓값
print(max(dp[n - 1]))
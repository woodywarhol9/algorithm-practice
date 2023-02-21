# 땅 : (N, 4)
# 각 행의 1 칸만 밟을 수 있고 -> 연속 열 불가
# 완전 탐색 -> 4^(100,000) : 시간 초과
# DP[n][k] = a[n][k] + max(a[n-1][k -1] + a[n-1][k-2] + a[n-1][k-3])
def solution(land):
    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    for i in range(len(land)):
        # 초기 성분 입력
        if i == 0:
            dp[0] = land[0]
            continue
        # DP 테이블 업데이트
        for j in range(4):
            dp[i][j] = land[i][j] + max([dp[i - 1][k] for k in range(4) if k != j])
    return max(dp[-1])
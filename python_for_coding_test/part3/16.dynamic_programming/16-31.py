"""
금광 : DP 구현이 익숙하지 않음. 다시 풀어보기!
"""

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    map_info = list(map(int, input().split()))
    
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(map_info[index:index + m])
        index += m
    
    # 다이나믹 프로그래밍 진행
    for j in range(1, m): # 첫번째 열은 이미 확인한 상태이므로 1부터 시작
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    # 최대 금액 확인
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    
    print(result)
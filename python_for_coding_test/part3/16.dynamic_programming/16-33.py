"""
퇴사 : 뒤쪽 날짜부터 거꾸로 확인. 아이디어!
"""
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 시간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # DP 테이블

# 상담 정보 입력
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 상담 날짜를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        # 저장해둔 max_value 할당 해주기
        dp[i] = max_value
    
print(max_value)


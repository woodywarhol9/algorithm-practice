n = int(input()) # 전체 상담 개수
t_list = [] # 상담 완료까지 기간
p_list = [] # 상담 완료 시 받을 수 있는 금액

dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    t, p = map(int, input().split())
    # 원소 추가
    t_list.append(t)
    p_list.append(p)

# DP 테이블 작성
for i in range(n - 1, -1, -1):
    time = t_list[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p_list[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
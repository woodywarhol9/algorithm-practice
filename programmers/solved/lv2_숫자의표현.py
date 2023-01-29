def solution(n):
    answer = 0
    # 누적합
    cum_sum = []
    for i in range(10001):
        cum_sum.append((i * (i + 1) // 2))
    # 확인
    for i in range(10001):
        for j in range(i + 1, 10001):
            if cum_sum[j] - cum_sum[i] == n:
                answer += 1
            elif cum_sum[j] - cum_sum[i] > n:
                break
    return answer
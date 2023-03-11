def solution(t, p):
    p_int, p_len, t_len = int(p), len(p), len(t)
    # i 범위 : t의 마지막 원소까지 채울 수 있도록
    answer = [t[i:i+p_len] for i in range(0, t_len - p_len + 1) if int(t[i:i+p_len]) <= p_int]
    return len(answer)
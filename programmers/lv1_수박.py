def solution(n):
    q, r = divmod(n, 2)
    return q * "수박" + r * "수"
def solution(n):
    m = n - 1
    for i in range(2, m + 1):
        if m % i == 0:
            return i
            
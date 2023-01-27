def solution(n):
    n_sqrt = n ** 0.5
    return (n_sqrt + 1) ** 2 if n_sqrt - int(n_sqrt) == 0 else -1
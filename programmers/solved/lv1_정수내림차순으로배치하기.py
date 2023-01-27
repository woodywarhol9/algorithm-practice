def solution(n):
    n_str = "".join(sorted(str(n), reverse = True))
    return int(n_str)
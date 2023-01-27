def to_ternary(n):
    ternary = ""
    while n:
        q, r = divmod(n, 3)
        n = q
        ternary += str(r)
    
    return ternary[::-1]

def solution(n):
    n_t = to_ternary(n)[::-1]
    return int(n_t, 3)
import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
memo = {0 : 1, 1 : 1}

def get_fact(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = n * get_fact(n - 1)
        return memo[n]

numerator = get_fact(n)
denominator = (get_fact(k) * get_fact(n - k))
print((numerator // denominator) % 10007)
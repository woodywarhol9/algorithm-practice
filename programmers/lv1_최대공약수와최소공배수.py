def get_gcd(a, b):
    while b!= 0:
        r = a % b
        a = b
        b = r
    return a

def solution(n, m):
    gcd = get_gcd(n, m)
    lcm = n * m / gcd
    return [gcd, lcm]

"""
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]
"""
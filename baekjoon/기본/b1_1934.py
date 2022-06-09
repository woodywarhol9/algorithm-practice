import sys

T = int(input())
"""
유클리드 호제법
"""
def euclidean(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a
        
for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    gcd = euclidean(A, B)
    lcm = (A * B) / gcd
    print(int(lcm))
    
import sys

dp = {}
def w(a, b, c):
    if (a, b, c) in dp:
        return dp[(a, b, c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            dp[(a, b, c)] = 1
        elif a > 20 or b > 20 or c > 20:
            dp[(a, b, c)] = w(20, 20, 20)
        elif a < b < c:
            dp[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) -\
                w(a, b - 1, c)
        else:
            dp[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) +\
                w(a - 1, b, c - 1) - w(a - 1, b - 1, c -1)
        return dp[(a, b, c)]

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
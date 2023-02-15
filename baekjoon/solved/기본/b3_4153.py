while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    a, b, c = sorted([a, b, c])
    print("right" if c*c == (a*a + b*b) else "wrong")
    
"""
두 원의 위치 관계를 이용.
"""
test_case = int(input())

for _ in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) **0.5
    # 2점에서 만나는 경우
    if abs(r1 - r2) < d and d < (r1 + r2):
        print(2)
    # 1점에서 만나는 경우
    # d == abs(r1 - r2)만 하게 되면 d =0, r1 = r2도 포함되기 때문에 조건 추가
    if d == r1 + r2 or (d == abs(r1 - r2) and d != 0):
        print(1)
    # 안 만나는 경우
    if d < abs(r1 - r2) or d > (r1 + r2):
        print(0)
    if d == 0 and r1 == r2:
        print(-1)
     
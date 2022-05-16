import sys

n, m = map(int, input().split())
# 제한 구간 정보
section_limit = [list(map(int, input().split())) for _ in range(n)]
section_test = [list(map(int, input().split())) for _ in range(m)]
#
speed_limit = []
for l, s in section_limit:
    speed_limit = speed_limit + [s for _ in range(l)]

speed_test = []
for l, s in section_test:
    speed_test =  speed_test + [s for _ in range(l)]

result = max([speed_test[i] - speed_limit[i] for i in range(100)])
print(result if result >= 0 else 0)
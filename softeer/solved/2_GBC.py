import sys

n, m = map(int, input().split())
# 제한 구간 정보
section_limit = [list(map(int, input().split())) for _ in range(n)]
# 테스트 구간 정보
section_test = [list(map(int, input().split())) for _ in range(m)]
# 제한 구간 정보 입력
speed_limit = []
for l, s in section_limit:
    speed_limit = speed_limit + [s for _ in range(l)]
# 테스트 구간 정보 입력
speed_test = []
for l, s in section_test:
    speed_test =  speed_test + [s for _ in range(l)]

result = max([speed_test[i] - speed_limit[i] for i in range(100)])
# 전부 속도를 지켰을 경우 음수니까 0 return
print(result if result >= 0 else 0)
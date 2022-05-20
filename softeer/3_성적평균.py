import sys
# 학생 수, 구간 수 입력
n, k = map(int, input().split())
# 성적 입력
score_list = list(map(int, input().split()))
# 구간 정보
k_info = [list(map(int, input().split())) for _ in range(k)]

for start, end in k_info:
    # 셋째자리에서 반올림
    result = round(sum(score_list[start - 1: end]) / (end - start + 1), 2)
    # 소수점 자리수
    print(f'{result:0.2f}')
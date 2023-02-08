# n, m, k, l
# nC1, mC1, kC1, lC1 -> n, m, k에 대한 선택
# 종류가 많은 경우 -> 시간 초과가 발생할 것 -> 어떻게 계산???...
from collections import defaultdict

def solution(clothes):
    # 조합의 개수
    answer = 1
    cloth_info = defaultdict(list)
    # type 별 옷 정리하기
    for c, c_type in clothes:
        cloth_info[c_type].append(c)
    # 옷 조합 = (해당 부위 옷을 입은 경우 + 안 입은 경우)
    for c_type, c in cloth_info.items():
        answer *= (len(c) + 1)
    # 아무것도 입지 않은 경우 제외
    answer -= 1
    return answer
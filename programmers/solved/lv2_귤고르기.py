# 귤 k 개 -> 서로 다른 종류 최소화!
# Counter 사용 후, 개수 기준 내림차순 정렬
from collections import Counter

def solution(k, tangerine):
    # 귤 종류 수
    tan_uniq = 0
    # 종류 별 개수 세기
    type_cnt = Counter(tangerine)
    type_cnt = sorted(type_cnt.values(), reverse = True)
    # 현재 귤의 개수
    tan_cnt = 0
    for cnt in type_cnt:
        tan_cnt += cnt
        tan_uniq += 1
        if tan_cnt >= k:
            break
        
    return tan_uniq
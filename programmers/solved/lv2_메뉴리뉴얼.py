# 각 손님들이 주문할 때, 가장 많이 함께 주문한 단품 메뉴를 코스 요리 메뉴로 구성
# 코스 요리 : 최소 2 가지 단품 + 최소 2 명의 손님이 주문했던 제품 만 포함
# 최종 -> 사전 순의 오름차순으로 정렬
 
# Orders 배열의 크기가 작고, orders 원소 크기 또한 작기 때문에 완전 탐색 가능
from itertools import combinations
 
def solution(orders, course):
    # 메뉴 저장
    set_menu = {}
    # n개의 조합 확인
    for i in course:
        # 각 주문 별 확인
        for order in orders:
            for comb in combinations(order, i):
                comb = sorted(comb)
                comb = "".join(comb)
                if comb not in set_menu:
                    set_menu[comb] = 0
                set_menu[comb] += 1
    # 개수 1개 이하로 주문된 세트는 제외
    set_menu = {foods:cnt for foods, cnt in set_menu.items() if cnt > 1}
    # 최대 개수 파악 위해, 코스 길이 순으로 정렬
    set_menu = sorted(set_menu.items(), key = lambda x : (len(x[0]), -x[1]))
    # 최대 개수 저장
    len_menu_cnt = dict(zip(course, [-1] * len(course))) 
    # 최대 개수 메뉴만 골라내기
    answer = []
    for foods, cnt in set_menu:
        # 해당 코스에서 최대인 경우만 저장
        if len_menu_cnt[len(foods)] <= cnt:
            len_menu_cnt[len(foods)] = cnt
            answer.append(foods)
    return sorted(answer)

# Counter를 활용해 코드를 간단히 표혀할 수 있다!
"""
from collections import Counter
from itertools import combinations
 
def solution(orders, course):
    result = []
 
    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
        # most_common : 개수 순으로 정렬하는 역할!
        most_ordered = Counter(order_combinations).most_common()
        # 최대 개수와 동일하지 않은 경우 필터링
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
    return [ ''.join(v) for v in sorted(result)]
"""
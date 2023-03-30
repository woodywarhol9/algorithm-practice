def solution(topping):
    # idx 별 케이크 가짓수 보관
    pt1_cnt, pt2_cnt = [], []
    # 나눈 케이크의 가짓수 확인
    pt1_unique, pt2_unique = set(), set()
    # pt1 케이크 확인
    for t in topping:
        pt1_unique.add(t)
        pt1_cnt.append(len(pt1_unique))
    # pt2 케이크 학인
    for t in topping[::-1]:
        pt2_unique.add(t)
        pt2_cnt.append(len(pt2_unique))
    # 비교를 위해서 역순으로 되돌리기
    pt2_cnt = pt2_cnt[::-1]
    return sum([1 for i in range(len(pt1_cnt) - 1) if pt1_cnt[i] == pt2_cnt[i + 1]])

"""
from collections import Counter
 
def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    res = 0
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            res += 1
    return res
"""
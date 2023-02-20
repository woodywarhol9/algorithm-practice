# 선행 스킬? 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬
# 중복이 없으니까, 필요없는 문자열 제거하면 될듯!
import re

def solution(skill, skill_trees):
    # 가능한 스킬 트리 개수
    cnt = 0
    # 확인할 스킬 정보 : 스킬 트리만 만족하면 되기 때문에!
    need_skill = list(skill)
    # 각 스킬 트리 확인
    for trees in skill_trees:
        check_skill = ""
        # 확인할 스킬만 따로 빼서 문자열 만들기
        for c in trees:
            if c in need_skill:
                check_skill += c
        # 스킬 트리와 일치하는지 확인 
        if skill[:len(check_skill)] == check_skill:
            cnt += 1
    return cnt
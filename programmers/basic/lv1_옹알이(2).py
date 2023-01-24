def solution(babbling):
    answer = 0
    for bab in babbling:
        # 비교할 문자열
        temp_c = ""
        # 이전에 나온 단어 확인
        prev_idx = -1
        for c in bab:
            temp_c +=c
            # 못 찾은 경우 중단
            if len(temp_c) > 4:
                break
            # 체크 시작
            for idx, word in enumerate(["aya", "ye", "woo", "ma"]):
                is_found = temp_c.find(word)
                # 이전 단어와 겹치지 않도록 찾은 경우
                if is_found == 0 and prev_idx != idx:
                    prev_idx = idx
                    temp_c = ""
        # 체크 성공
        if not temp_c:
            answer += 1
    return answer
# 문자열 함수 활용하기
"""
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if not i.rstrip():
            answer +=1
    return answer
"""
# 정규 표현식 활용하기
"""
import re

def solution(babbling):
    answer = 0
    # () : 그룹 지정, \1 : 캡쳐된 그룹 참조
    re_pt1 = r"(aya|ye|woo|ma)\1+"
    re_pt2 = r"^(aya|ye|woo|ma)+$"
    for i in babbling:
        if not re.search(re_pt1, i) and re.search(re_pt2, i):
            answer += 1
    return answer
"""

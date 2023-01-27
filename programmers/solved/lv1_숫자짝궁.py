from collections import Counter
import re

def solution(X, Y):
    answer = []
    # 문자열로 변경
    X, Y = map(str, (X, Y))
    # 공통 숫자 확인
    com_num = sorted(set(X) & set(Y), reverse = True)
    # 없을 경우 -1 리턴
    if not com_num:
        return "-1"
    # 성분 개수 세기
    cnt_X, cnt_Y = Counter(X), Counter(Y)
    # 공통 문자 있는 경우
    for i in com_num:
        answer.extend([i] * min(cnt_X[i], cnt_Y[i]))
    answer = "".join(answer)
    # 0이 여러개인 경우 0으로 처리
    answer = re.sub("^0+", "0", answer)
    
    return answer
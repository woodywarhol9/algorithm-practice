# 10일 동안 회원 자격
# 회원 : 하루 1 개만
# 10일 연속 일치할 경우에 가입 !
from collections import Counter

def solution(want, number, discount):
    best_day = 0
    want_number = dict(zip(want, number))
    # 언제 가입하면 좋을 지 확인
    for i in range(len(discount) - 10 + 1):
        # 동일할 경우 증가
        if want_number == Counter(discount[i:i + 10]):
            best_day += 1
    return best_day
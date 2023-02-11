# Hash를 활용한 풀이
def solution(phone_book):
    # 번호 저장
    phone_hash = set(phone_book)
    for phone in phone_book:
        temp_num = ""
        # 앞 자리의 숫자부터 추가하면서, 저장된 번호가 있는지 확인
        for digit in phone:
            temp_num += digit
            if temp_num in phone_hash and temp_num != phone:
                return False
    return True
# 정렬을 활용한 풀이
"""
def solution(phone_book):
    answer = True
    # 문자열 정렬
    phone_book.sort()
    for i in range(len(phone_book)-1):
    	# 같은 문자(숫자) 기준으로 정렬 됐기 때문에, 앞 뒤만 비교하면 됨!
        if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            answer = False
            break
    return answer
"""
# 초기 풀이 : 시간 초과!
"""
# 접두어 여부 확인
# 접두어? (최대 단어 길이 -1) 까지만 접두어가 될 수 있음
# 접두어 탐색 범위 : 나보다 길이가 더 긴 단어들만 확인 가능
# 길이에 따라서, 접두어 후보를 나누고, 이후 비교하면?
# 최대 20 * N -> 시간 초과 X
from collections import defaultdict

def solution(phone_book):
    # 전화 번호 길이 확인 
    phone_len = defaultdict(list)
    for i in phone_book:
        phone_len[len(i)].append(i)
    # 접두사 여부 확인
    while phone_len:
        min_len = min(phone_len.keys())
        prefix = phone_len[min_len]
        del phone_len[min_len]
        # 20 * 5만 * 5만 = 시간 초과
        for _, phone in phone_len.items():
            for p in phone:
                for pre in prefix:
                    # 접두사면, 처음 위치에서 발견됨
                    if p[:min_len] == pre:
                        return False    
    return True
"""
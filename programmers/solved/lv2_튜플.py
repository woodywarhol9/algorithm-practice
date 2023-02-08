# 원소의 개수가 n, 중복되는 원소가 없는 튜플
# 튜플은 원소의 순서를 고려해야 함 -> 집합의 개수가 늘어날 수록 1 개 씩 추가 됨
# 이를 통해 튜플 원소의 순서를 알 수 있다!
import re

def solution(s):
    # 최종 반환할 튜플
    answer = []
    s = s[1:-1]
    # 중복 문자열 확인
    char_set = set()
    # 길이에 따라 정렬하기 위해 문자열 저장
    s_list = []
    for word in re.findall(r"{[0-9]+[,0-9]*}", s):
        # 중괄호 제거 + ','를 기준으로 숫자 나누기
        word = word[1:-1].split(",")
        s_list.append(word)
    # 길이에 따라 정렬
    s_list.sort(key = lambda x : len(x))
    # 원래 튜플 반환하기
    for word in s_list:
        for char in word:
            if char not in char_set:
                char_set.add(char)
                answer.append(int(char))
    return answer
# 자카드 유사도 : (두 집합의 교집합 크기 / 두 집합의 합집합 크기
# 중복 문자에 대해서도 처리 가능
# 둘다 공집합인 경우 -> 1로 정의
from collections import Counter

def solution(str1, str2):
    # 공집합일 경우 생각해서 1로 초기화
    j_sim = 1
    # 소문자로 변경
    str1, str2 = str1.lower(), str2.lower()
    # 원소 만들기
    str1 = [str1[i:i + 2] for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i + 1].isalpha()]
    str2 = [str2[i:i + 2] for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i + 1].isalpha()]
    # 원소 개수 세기
    str1 = Counter(str1)
    str2 = Counter(str2)
    # 분모, 분자 원소 구하기
    divisor = set(str1.keys()) | set(str2.keys())
    dividend = set(str1.keys()) & set(str2.keys())
    # 분모, 분자 값 결정하기
    divisor = sum([max(str1[i], str2[i]) for i in divisor])
    dividend = sum([min(str1[i], str2[i]) for i in dividend])
    if divisor != 0:
        j_sim = dividend / divisor
    # 결과 조건에 맞도록
    j_sim *= 65536
    j_sim = int(j_sim)
    
    return j_sim
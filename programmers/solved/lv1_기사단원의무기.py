from collections import defaultdict
from math import prod

# 약수 개수 구하기 1 : 소인수 분해 활용
def solution(number, limit, power):
    # 숫자 1 고려해서 초기 값 1로 설정
    answer = [1]
    for i in range(2, number + 1):
        # 소인수 분해 결과 저장 : 각 약수의 개수
        prime_cnt = defaultdict(int)
        for j in range(2, int(i ** 0.5) + 1):
            while i % j == 0:
                prime_cnt[j] += 1
                i //= j
        if i != 1:
            prime_cnt[i] += 1
        answer_temp = prod([k + 1 for k in prime_cnt.values()])
        answer.append(answer_temp)
    # 파워 제한
    answer = sum([i if i <= limit else power for i in answer])
    return answer
"""
# 약수 개수 구하기 2 : 약수의 정의 활용
def solution(number, limit, power):
    answer = 1
    # 약수 검사
    for i in range(2, number + 1):
        answer_temp = set()
        for j in range(1, int(i ** 0.5) + 1):
            # 약수라면
            if i % j ==0:
                answer_temp.add(j)
                answer_temp.add(i // j)
        # 파워 리밋 적용
        answer += len(answer_temp) if len(answer_temp) <= limit else power
    return answer
"""
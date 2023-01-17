# 정수 번호의 합이 0 인 경우, 삼총사
from itertools import combinations

def solution(number):
    answer = 0 
    combi = combinations(number, 3)
    for com in combi:
        if sum(com) == 0:
            answer += 1
    return answer
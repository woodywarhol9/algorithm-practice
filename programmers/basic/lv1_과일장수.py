# 점수가 가장 낮은 사과가 가격을 결정
# 따라서 점수가 높은 사과끼리 묶어야 최대 가격 설정 가능
def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    # idx 대소 비교 과정에서 계속 계산되기 때문에 미리 계산
    score_len = len(score)
    # 내림차순으로 정렬하면, 묶음에서 가장 가치 없는 사과가 마지막 idx에 위치하게 됨
    answer = [score[i + m - 1] * m for i in range(0, score_len, m) if (i + m - 1) < score_len]
    return sum(answer)
def solution(dartResult):
    option = ["*", "#"]
    score = list(map(str,range(0, 10)))
    region = ["S", "D", "T"]
    
    cur_option = [0, 0, 0]
    cur_score = []
    # 점수 계산
    for idx, c in enumerate(dartResult):
        if c in score:
            cur_score.append(int(c))
        elif c in region:
            # 10이 입력된 경우
            if dartResult[idx - 1].isdigit() and dartResult[idx - 2].isdigit():
                pop = cur_score.pop()
                cur_score[-1] = int(str(cur_score[-1]) + str(pop))
            cur_score[-1] = cur_score[-1] ** (region.index(c) + 1)
        elif c in option:
            cur_option[len(cur_score) - 1] = c
    # 옵션 적용
    for j in range(3):
        if j == 0 and cur_option[0] == "*":
            cur_score[0] *= 2
        else:
            if cur_option[j] == "*":
                cur_score[j] *= 2
                cur_score[j - 1] *= 2
            elif cur_option[j] == "#":
                cur_score[j] *= -1
    
    return sum(cur_score)

"""
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
"""
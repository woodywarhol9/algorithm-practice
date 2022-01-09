 """
 실패율 : 효율성도 신경써서 풀자. 
 """
 def solution(N, stages):
    answer = []
    length = len(stages)
    
    for stage in range(1, N+1):
        count = stages.count(stage)
        if count == 0:
            fail = 0
        else :
            fail = count / length
        answer.append((stage, fail))
        length -= count
    
    answer = sorted(answer, key = lambda x : x[1], reverse = True)
    answer = [x[0] for x in answer]
    
    return answer

# 런타임 에러 코드 : 비효율적...
"""
def solution(N, stages):
    answer = []
    
    for stage in range(1, N+1):
        stage_player_num = len([x for x in stages if x >= stage])
        unclear_player_num = stages.count(stage)
        if stage_player_num == 0:
            answer.append((stage, 0))
        answer.append((stage, unclear_player_num / stage_player_num))
    
    answer = sorted(answer, key = lambda x : x[1], reverse = True)
    answer = [x[0] for x in answer]
    return answer
"""